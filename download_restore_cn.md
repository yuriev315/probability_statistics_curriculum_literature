# 下载与还原说明

马尔科夫决策过程（MDP）与序贯决策资源库：论文、教材、课程资料、官方软件文档离线网页、参考项目源码快照，以及 13 个参考项目的 Windows 最小运行依赖。

## 附件

文件名前缀都是 `markov_decision_process_resources_20261106_`。

| 附件 | 内容 |
|---|---|
| `batch001_cn_en.tar` | 资料库本体：论文、教材、课程、软件文档、项目快照、目录、指南和脚本 |
| `manifests_cn_en.tar.gz` | 运行依赖的说明、依赖清单、运行报告和 `.url` 占位文件，请先下载 |
| `windows_py37_cn_en.tar` | Windows x64 + Python 3.7 的 wheel（Spinning Up） |
| `windows_py310_cn_en.tar` | Windows x64 + Python 3.10 的 wheel |
| `windows_py312_cn_en.tar` | Windows x64 + Python 3.12 的 wheel |
| `source_cn_en.tar` | 12 个参考项目的源码快照（`.tar.gz`） |
| `sdist_cn_en.tar` | 只有源码包的依赖和 d4rl 快照 |

另有 `archive_index_cn.csv`（每个文件所在的附件、大小、SHA-256 和许可）、`release_excluded_cn.csv`（只提供 `.url` 的资料及原因）和 `SHA256SUMS.txt`（附件校验值）。

## 还原

所有 tar 包的顶层目录都是 `markov_decision_process_resources/`，解压到同一个目录即可合并：

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing
for f in markov_decision_process_resources_20261106_*.tar; do tar -xf "$f"; done
tar -xzf markov_decision_process_resources_20261106_manifests_cn_en.tar.gz
```

Windows 10 及以上可以用自带的 `tar`：

```powershell
Get-ChildItem markov_decision_process_resources_20261106_*.tar | ForEach-Object { tar -xf $_.FullName }
tar -xzf markov_decision_process_resources_20261106_manifests_cn_en.tar.gz
```

只需要阅读资料时，下载 `batch001_cn_en.tar` 就够了；目录见 `catalog_cn.csv`，学习路线见 `guides/`。运行参考项目时再下载其余附件，步骤见 `projects_13/README_cn.md` 和 `reports/final_report_cn.md`。

## `.url` 占位文件

版权页保留全部权利、未声明许可证或 arXiv 默认许可的资料不随包分发，原位置放一个同名 `.url` 文件，里面是官方下载地址，PDF 还记录了原文件的大小和 SHA-256，下载后可以核对。超过 100 MiB 的依赖（torch、Julia）也是 `.url`。

## 许可

各文件保留其上游许可证，NC、ND 等限制仍然有效，逐个文件的许可见 `archive_index_cn.csv`。如果你是权利人并希望移除某个文件，请提 Issue。
