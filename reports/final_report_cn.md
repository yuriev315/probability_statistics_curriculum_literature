# 马尔科夫决策过程资源库：13 个参考项目运行报告

日期：2026-11-05。

## 最终运行状态：RUNNABLE_WITH_URL_PLACEHOLDERS

13 个参考项目里，11 个在 Linux 上测试通过，其中 Spinning Up 只测了部分模块。运行用到 torch 的项目前要先按 `.url` 下载 torch。POMDPs.jl 没有运行，**没有任何项目在 Windows 上实际运行过**。

| 项目状态 | 数量 | 项目 |
|---|---|---|
| RUNNABLE_VERIFIED | 4 | Gymnasium、PettingZoo、OpenSpiel、pymdptoolbox |
| RUNNABLE_WITH_URL_PLACEHOLDERS | 5 | Stable-Baselines3、TorchRL、d3rlpy、OmniSafe、CleanRL（都要先下载 torch） |
| DEPENDENCIES_INCOMPLETE | 2 | CORL（没有 mujoco-py 和 D4RL 数据集）、POMDPs.jl（Julia 只有 `.url`，包要联网安装） |
| NOT_TESTED | 2 | Spinning Up（完整环境要 Python 3.7）、decisionmaking（只有 README，没有代码） |

适用的限制：下载并保留的原文件单个不超过 100 MiB；Release 单个资产可到约 1.5 GB。

## 1. 目录

- 资料库全文与 13 个项目快照：Release `mdp-20261106` 的 `markov_decision_process_resources_20261106_batch001_cn_en.tar`
- 项目环境：`projects_13/`，使用说明见 `projects_13/README_cn.md`
- 资料库脚本：标签内的 `scripts/`

## 2. Python 环境

| 环境 | 项目 |
|---|---|
| Windows x64 + Python 3.7 | Spinning Up（TensorFlow 1.15） |
| Windows x64 + Python 3.10 | Stable-Baselines3、TorchRL、d3rlpy、OmniSafe、CleanRL、CORL、pymdptoolbox，以及仓库脚本 |
| Windows x64 + Python 3.12 | Gymnasium、PettingZoo、OpenSpiel（源码要求 3.11 以上） |
| Julia 1.13 | POMDPs.jl |

全部是 CPU 版。

## 3. 依赖

依赖来自各项目的实际 import 和声明，不含可选功能和开发工具，见 `manifests/minimum_runtime_dependencies.csv`。每个项目的版本清单在 `projects_13/envs/<环境>/requirements/`。7 个库都固定到了和源码快照一致的版本。

测试和解析中查出的问题：

- **d3rlpy** 不固定版本时会解析到古老的 0.1，已固定为源码对应的 2.8.1。
- **OmniSafe** 不固定 numpy 时 pandas 2.0.3 和 numpy 2.2.6 不兼容，导入直接失败，已固定 `numpy<2`。
- **CleanRL** 声明 Python 低于 3.11，并固定 torch 2.4.1。
- **CORL** 依赖 Git 上的 `d4rl`，已单独下载快照；`mujoco-py` 需要编译和 MuJoCo，没有提供。
- **Spinning Up** 的 `setup.py` 写 torch 1.3.1，没有 Windows wheel，这里用了 1.13.1，兼容性未验证。

## 4. 已知问题

- 仓库脚本的 `scripts/common_en.py` 第 10 行 `import fcntl` 在 Windows 上会失败，可用 `runtime/windows_compat/fcntl.py` 替代，未在 Windows 上运行过；第 27、31 行有硬编码的 `/root/.cache` 路径。这些都没有修改原文件。
- decisionmaking 仓库只有 README，不是代码项目。

## 5. 测试结果

13 个项目：通过 11，受阻 1，不适用 1，全部在 Linux 隔离环境里进行，见 `manifests/runtime_test_results.csv`。

- **实际运行（7 个）**：Gymnasium 跑 CartPole，Stable-Baselines3 训练 PPO 64 步，CleanRL 跑完 `ppo.py` 128 步，d3rlpy 离线训练 DQN 4 步，OpenSpiel 下完一局井字棋，pymdptoolbox 用值迭代求解，TorchRL 跑一次前向计算。
- **只测导入（3 个）**：PettingZoo、OmniSafe、CORL。
- **只测部分模块（1 个）**：Spinning Up。这台机器没有 Python 3.7，所以跳过包的初始化，在 Python 3.10 上测了 PyTorch 核心模块，不代表完整环境可用。
- **受阻（1 个）**：POMDPs.jl。本机没有 Julia，运行外部程序的步骤之前已被权限系统拒绝，这次没有再尝试。
- **不适用（1 个）**：decisionmaking。

仓库脚本：4 个模块能导入，5 个脚本语法通过，`build_catalog_en.py` 在临时副本生成的目录与仓库中的 `catalog_cn.csv` 逐字节相同。

没有复现任何论文结果，也没有长时间训练。

## 6. 数据集和模型

运行环境里没有下载数据集和模型。CORL 需要的 D4RL 数据集和 MuJoCo 环境要另外准备。

## 7. `.url` 占位符

共 6 个，全部直接请求验证有效，见 `manifests/url_placeholders.csv`。

| 文件 | 大小 | 说明 |
|---|---|---|
| torch 2.12.1 / 2.4.1 / 1.13.1（Windows CPU） | 117 / 192 / 157 MiB | 用到 torch 的项目需要 |
| Julia 1.13.3（Windows 安装包 / Linux） | 164 / 289 MiB | POMDPs.jl 需要 |
| 原 Release 第 1 包 | 1.07 GiB | 全文和原始项目快照 |

## 8. 缺失项

Windows 实机测试、Julia 运行验证、Python 3.7 完整环境验证、mujoco-py、D4RL 数据集、GPU。明细见 `manifests/missing_requirements.csv`。

## 9. 清理候选

`manifests/cleanup_candidates.csv` 列出采集和测试时的本地记录目录，它们不在发布内容中。

## 10. 磁盘占用

- 项目约 739M，其中 `projects_13/` 约 735M
- 没有下载论文全文和数据集

全部文件的校验和见 `manifests/checksums.sha256`。wheel 下载时都核对了上游 SHA256；GitHub 快照上游没有提供 SHA256，只记录实际值，并做了完整性检查。

## 11. 发布内容

Release `mdp-20261106` 的运行依赖附件：`windows_py37`、`windows_py310`、`windows_py312`、`source`、`sdist` 五个 tar 包和 `manifests_cn_en.tar.gz`。下载的原文件与 `manifests/download_status.csv` 记录的 SHA-256 逐一相同。

2 个未声明许可证的文件只提供 `.url`：`gym 0.15.7` 源码包和 decisionmaking 仓库快照（只有 README）。逐个文件的许可证见 `manifests/release_file_licenses.csv`。

## 12. 安装和运行

Windows + Python 3.12（未实测）：

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python -m pip install --no-index --find-links projects_13\envs\windows_py312\wheelhouse -r projects_13\envs\windows_py312\requirements\Farama_Gymnasium.txt
.venv\Scripts\python -c "import gymnasium as g; e=g.make('CartPole-v1'); print(e.reset(seed=0)[0])"
```

其他项目的步骤见 `projects_13/README_cn.md`。
