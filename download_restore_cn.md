# 下载与解压

Release `reinforcement-learning-20261106` 的附件分两部分：资源库全文和运行环境。所有附件都以 `reinforcement_learning_resources_20261106_` 开头。

| 附件 | 内容 |
|---|---|
| `..._batch001_cn_en.tar` | 资源库全文：首页 `index_cn.html`、目录与登记表、中文指南、脚本、15 个子方向的论文、教材、课程讲义与课程网页、官方软件文档网页、19 个参考项目源码快照 |
| `..._runtime_windows_min*.tar` | Windows 10/11 x64：每个项目基础依赖的 wheel 与安装脚本 |
| `..._runtime_windows_rest*.tar` | Windows：其余依赖分组的 wheel |
| `..._runtime_ubuntu*.tar` | Ubuntu x86_64：wheel 与安装脚本 |
| `..._runtime_models_datasets*.tar` | 项目引用的小模型配置和样例数据 |
| `..._runtime_docs*.tar` | 运行环境说明 `runtime/README_cn.md`、登记表和工具脚本 |
| `archive_index_cn.csv` | 每个附件内的每个文件：相对路径、字节数、SHA-256 |
| `release_excluded_cn.csv` | 只提供 `.url` 链接的条目、原因和官方地址 |
| `windows_rename_map_cn.csv` | 为 Windows 改名的文件和离线化新增的文件 |
| `SHA256SUMS.txt` | 附件本身的 SHA-256 |

## 下载

```bash
gh release download reinforcement-learning-20261106 \
  --repo yuriev315/probability_statistics_curriculum_literature \
  --dir rl_dl --pattern "reinforcement_learning_resources_20261106_batch*" --pattern "SHA256SUMS.txt"
cd rl_dl && sha256sum -c --ignore-missing SHA256SUMS.txt
```

Windows 上可在浏览器中逐个下载，再用 `certutil -hashfile <文件> SHA256` 对照 `SHA256SUMS.txt`。

## 解压

把需要的 tar 包解压到同一个目录（Linux 用 `tar -xf`，Windows 10/11 可直接用系统自带的 `tar -xf`）：

```bash
mkdir -p reinforcement_learning_resources && cd reinforcement_learning_resources
for f in ../rl_dl/*.tar; do tar -xf "$f"; done
```

解压后用浏览器打开 `index_cn.html`。每个文件的 SHA-256 记在 `archive_index_cn.csv`，可以逐个核对。

## `.url` 文件

版权页保留全部权利的教材、未声明再分发许可的课程讲义和课程网页、arXiv 默认许可的论文，以及许可不允许公开分发的少数 wheel，只提供 `.url` 链接：在 Windows 上双击即可打开官方地址，在其他系统上用文本编辑器打开，`URL=` 后面就是地址。这些条目的原因和地址汇总在 `release_excluded_cn.csv`、`runtime/manifests/url_placeholders_cn.csv`。

单个超过 100 MiB 的 wheel 和模型权重同样只有 `.url`，文件中写有下载命令和 SHA-256。

## 运行环境

安装步骤见运行环境附件中的 `runtime/README_cn.md`。项目源码在资源库的 `projects/` 目录，与运行环境分开下载。
