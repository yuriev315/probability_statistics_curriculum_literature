# 运行环境（Windows 10/11 x64 与 Ubuntu）

本部分是资源库中 19 个参考项目（`projects/`）的最小运行依赖：每个项目一组基础依赖锁定文件、离线安装脚本和对应的 wheel，外加项目引用的少量模型配置和样例数据。附件都以 `reinforcement_learning_resources_20261106_runtime_` 开头。

| 附件 | 内容 |
|---|---|
| `reinforcement_learning_resources_20261106_runtime_windows_min*.tar` | Windows：每个项目基础依赖用到的 wheel、`windows/min_projects/` 安装脚本 |
| `reinforcement_learning_resources_20261106_runtime_windows_rest*.tar` | Windows：其余依赖分组（extras、文档、测试等）用到的 wheel |
| `reinforcement_learning_resources_20261106_runtime_ubuntu*.tar` | Ubuntu x86_64：wheel 与 `ubuntu/projects/` 安装脚本 |
| `reinforcement_learning_resources_20261106_runtime_models_datasets*.tar` | 项目引用的小模型配置、分词器和样例数据（`run_data/`） |
| `reinforcement_learning_resources_20261106_runtime_docs*.tar` | 本说明、`manifests/` 登记表、生成这些文件的工具脚本 |

附件内的路径都以 `runtime/` 开头，可以和资源库全文解压到同一个目录（例如 `D:\rl`），不会互相覆盖。项目源码在资源库的 `projects/` 目录（`batch` 附件）。

```bat
mkdir D:\rl\dl
gh release download reinforcement-learning-20261106 --repo yuriev315/probability_statistics_curriculum_literature --dir D:\rl\dl --pattern "reinforcement_learning_resources_20261106_runtime_windows_min_*" --pattern "reinforcement_learning_resources_20261106_runtime_docs_*"
cd /d D:\rl
for %f in (dl\*.tar) do tar -xf "%f"
```

## Windows：基础依赖

安装 64 位 CPython（大多数项目用 3.10 或 3.11，版本写在 `.bat` 第一行），然后在空目录中运行：

```bat
mkdir D:\work\P-01 & cd /d D:\work\P-01
D:\rl\runtime\windows\min_projects\P-01\install_base.bat
.venv_P-01\Scripts\activate.bat
```

缺 wheel 时 `.bat` 会停止并给出下载命令（`runtime\windows\download_missing_wheels.ps1 -Project P-01`）。其他依赖分组的脚本在 `runtime\windows\all_projects\<编号>\`，GPU 版本在 `runtime\windows\projects\<编号>\`。

## Ubuntu

```bash
mkdir -p ~/work/P-01 && cd ~/work/P-01
bash /path/to/rl/runtime/ubuntu/projects/P-01/install_base.sh
. .venv_P-01/bin/activate
```

缺 wheel 时运行 `bash /path/to/rl/runtime/ubuntu/download_wheels_all.sh P-01`。

## 覆盖情况

- 16 个项目选定了基础依赖，见 `manifests/min_project_dependencies_cn.csv`；P-08 d3rlpy、P-09 CORL、P-13 Decision Transformer 的锁定依赖在 Windows 上无解，未选。
- 单个超过 100 MiB 的 wheel（主要是 `torch` 和 CUDA 库）只有 `.url`，按其中的命令下载并校验 SHA-256。
- NVIDIA CUDA 运行库、`nvidia_mathdx`、`craftground_runtime` 的条款不允许公开再分发，只提供 `.url`。
- 模型权重都超过 100 MiB，只有 `.url`；数据集只有样例。D4RL、Minari、Atari ROM 等由项目运行时自行下载。
- 每个 wheel 的许可、大小、SHA-256 和所在附件见 `manifests/runtime_wheels_cn.csv`；全部占位链接见 `manifests/url_placeholders_cn.csv`。

## 验证情况

| 检查 | 结果 |
|---|---|
| Ubuntu 离线安装基础依赖并 `pip check` | 5 个项目通过：P-01, P-05, P-06, P-07, P-20 |
| Windows 安装脚本 | 未在 Windows 主机上实际运行 |
| 运行项目代码 | 未运行 |
