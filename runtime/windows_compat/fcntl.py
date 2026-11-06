"""No-op stand-in for the POSIX-only fcntl module, for running the repository scripts on Windows.
The scripts use flock only to share a rate limit between processes, so with this stand-in run one process at a time."""
LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8
def flock(fd, operation):
    return None
def lockf(fd, cmd, len=0, start=0, whence=0):
    return None
