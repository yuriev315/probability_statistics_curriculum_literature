# 33 份实践材料的运行依赖（Windows x64）

依赖在 Release `probstat-resources-20261105` 中，把附件解压到仓库根目录：

- `windows_py310`：100 个 Python 3.10 wheel
- `r_windows`：R 4.6.2 安装包和 585 个 CRAN Windows 二进制包（含 `PACKAGES` 索引）
- `sdist`：`l0bnb` 源码包，安装时需要编译

材料源码在 Release `probstat-files-20261105` 的 `practice_source` 附件里，位于 `projects_33/source/`。没有声明许可证的材料不公开，只有 `practice/` 下的 `.url`，要先按链接下载。

## 安装

Python（把 `PROJECT` 换成 `requirements` 目录里的材料名）：

```bat
py -3.10 -m venv .venv
.venv\Scripts\pip install --no-index --find-links projects_33\envs\windows_py310\wheelhouse -r projects_33\envs\windows_py310\requirements\PROJECT.txt
```

ISLP Labs 还需要 `torch`：先按 `wheelhouse/*.whl.url` 下载到 `wheelhouse`。

R（先运行 `R-4.6.2-win.exe`，再在 R 里执行，把 `PKG` 换成包名；`contriburl` 用解压后的绝对路径）：

```r
install.packages("PKG", repos = NULL, contriburl = "file:///C:/path/to/projects_33/r_windows/contrib", type = "win.binary")
```

MIT 18.338 需要 Julia，按 `native/julia/*.url` 下载。

## 验证情况

- wheel 的 SHA-256 与 PyPI 一致；14 个 `*.lock.txt` 都用 `pip install --dry-run --require-hashes --platform win_amd64 --python-version 3.10` 检查通过（ISLP 不含 `torch`）。
- R 包通过了 zip 校验和包内 `MD5` 校验。CRAN 的 Windows 索引没有 MD5，所以没有和索引比对。
- **没有实际运行过这些材料，也没有在 Windows 上运行过。**
- 依赖来自对源码 import 和 library 语句的静态扫描，可能有遗漏。部分材料需要的包不在 CRAN，见 `r_projects.json` 的 `not_on_cran`，其中有些是扫描误判。

每个文件的许可证和校验值见 `release_files_cn.csv`。
