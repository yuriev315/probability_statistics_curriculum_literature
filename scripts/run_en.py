#!/usr/bin/env python3
"""Resume-safe runner for the MDP resource library.

  python3 -I scripts/run_en.py books
  python3 -I scripts/run_en.py courses
  python3 -I scripts/run_en.py software
  python3 -I scripts/run_en.py projects
  python3 -I scripts/run_en.py papers            # all categories
  python3 -I scripts/run_en.py papers 04         # one category
  python3 -I scripts/run_en.py catalog
  python3 -I scripts/run_en.py status
  python3 -I scripts/run_en.py all               # materials then papers then catalog

Already-verified items are skipped. Failed items are skipped unless --retry-failed.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = [sys.executable, "-I"]
CATS = [f"{i:02d}" for i in range(1, 13)]


def run(args):
    print("+", " ".join(args), flush=True)
    r = subprocess.run(args, cwd=str(ROOT))
    if r.returncode:
        sys.exit(r.returncode)


def main():
    a = sys.argv[1:]
    retry = "--retry-failed" in a
    a = [x for x in a if x != "--retry-failed"]
    extra = ["--retry-failed"] if retry else []
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = a[0]
    if cmd in ("books", "courses", "software", "projects"):
        run(PY + ["scripts/materials_en.py", "fetch", cmd] + extra)
    elif cmd == "papers":
        cats = a[1:] or CATS
        for c in cats:
            run(PY + ["scripts/papers_en.py", "download", c, "--target", "12"] + extra)
    elif cmd == "catalog":
        run(PY + ["scripts/build_catalog_en.py"])
    elif cmd == "status":
        run(PY + ["scripts/materials_en.py", "status"])
        run(PY + ["scripts/papers_en.py", "status"])
    elif cmd == "all":
        for s in ("books", "courses", "software", "projects"):
            run(PY + ["scripts/materials_en.py", "fetch", s] + extra)
        for c in CATS:
            run(PY + ["scripts/papers_en.py", "download", c, "--target", "12"] + extra)
        run(PY + ["scripts/build_catalog_en.py"])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
