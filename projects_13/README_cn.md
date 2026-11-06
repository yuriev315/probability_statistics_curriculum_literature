# 13 个参考项目的最小运行环境

资料库 `projects/` 里的 13 个参考项目（快照在 Release `mdp-20261106` 的 `markov_decision_process_resources_20261106_batch001_cn_en.tar` 中）。这里只保留运行它们需要的基础依赖（CPU），可选功能、开发工具、GPU 版和数据集不在内。

每个项目用哪个环境、测到什么程度，见 `manifests/project_status.csv`；逐包依赖见 `manifests/minimum_runtime_dependencies.csv`。

## 目录

```
projects_13\
├─ source\               12 个项目的源码快照（decisionmaking 只有 .url）
├─ envs\windows_py37\    Windows x64 + Python 3.7（Spinning Up）
├─ envs\windows_py310\   Windows x64 + Python 3.10
├─ envs\windows_py312\   Windows x64 + Python 3.12
│    ├─ wheelhouse\      wheel；torch 超过 100 MiB，只有 .whl.url
│    └─ requirements\    <项目>.in、<项目>.txt
├─ sdist_needs_build\    只有源码包的依赖和 d4rl，需要构建
└─ native\julia\         Julia 的 .url
```

## 环境分配

| 环境 | 项目 |
|---|---|
| Python 3.7 | Spinning Up |
| Python 3.10 | Stable-Baselines3、TorchRL、d3rlpy、OmniSafe、CleanRL、CORL、pymdptoolbox |
| Python 3.12 | Gymnasium、PettingZoo、OpenSpiel |
| Julia 1.13 | POMDPs.jl |
| 无需运行 | decisionmaking（只有 README） |

## 安装一个 Python 项目

用到 torch 的项目：先打开 `wheelhouse\` 里的 `.whl.url` 下载文件，放回同一目录，并核对其中的 `SHA256=`。

Windows + Python 3.10（以 Stable-Baselines3 为例）：

```powershell
py -3.10 -m venv .venv
.venv\Scripts\python -m pip install --no-index --find-links projects_13\envs\windows_py310\wheelhouse --find-links projects_13\sdist_needs_build -r projects_13\envs\windows_py310\requirements\DLR_RM_stable_baselines3.txt
```

其他版本把命令里的版本和环境名换成对应的即可。

CleanRL、CORL、pymdptoolbox、Spinning Up 不是安装包：解压 `source\` 里的快照，在解压目录下运行。例如 CleanRL：`python cleanrl\ppo.py --total-timesteps 128 --num-envs 1 --num-steps 32 --num-minibatches 2 --update-epochs 1 --no-cuda`。

依赖源码包（如 `gym`、`gast`）的项目，构建时需要 setuptools 和 wheel。

## POMDPs.jl

按 `native\julia\` 里的 `.url` 安装 Julia，然后解压 `source\` 里的快照，在里面运行：

```
julia --project=. -e "using Pkg; Pkg.instantiate(); using POMDPs"
```

这一步需要联网，Julia 依赖没有离线准备，也没有实测过。

## 局限

- Windows 上没有实际运行过。
- 研究项目只测了导入或很短的训练，没有复现论文结果。
- CORL 没有 mujoco-py 和 D4RL 数据集，不能真正训练。
- Spinning Up 的完整环境（Python 3.7 + TensorFlow 1.15）没有测过，只测了 PyTorch 核心模块。
- `setup.py` 写的 torch 1.3.1 没有 Windows wheel，所以用了 1.13.1，和原代码的兼容性未验证。
