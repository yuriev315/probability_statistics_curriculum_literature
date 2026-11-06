# 算法地图

把方法对应到本库教材、论文与源码。代码等级：L0 已下载；L1 静态核对入口/许可证/配置。本轮未执行。

## 精确动态规划（有限 MDP，已知模型）

| 方法 | 教材/课程 | 论文 | 源码 |
|---|---|---|---|
| 策略评估 | Sutton 第 4 章；6.231 | — | `projects/sawcordwell_pymdptoolbox_en` |
| 策略迭代 | 同上；Bertsekas Course in RL | `03_.../1910.00120` rollout | pymdptoolbox；ADM Julia `projects/algorithmsbooks_decisionmaking_en` |
| 价值迭代 | Sutton 4.4；ADM 第 7 章 | Li 概览 `03_.../1701.07274` | 同上 |
| LP 表述 | Boyd；Bertsekas Convex Theory | — | 小型 MDP 可自写 LP；无独立求解器包 |

收敛：Abstract DP 3e。复杂度：状态–动作乘积，表格法指数爆炸。

## 无模型价值方法

| 方法 | 要点 | 资料 | 源码 |
|---|---|---|---|
| MC 策略评估 | 无自举，需终止 | Sutton 第 5 章 | Spinning Up 文档/代码中的 VPG 回报估计 |
| TD(0)/TD(λ) | 自举、资格迹 | Sutton 第 6、12 章；1988 Sutton PDF | — |
| SARSA | 同轨 | Sutton 第 6 章 | SB3 无独立 SARSA；CleanRL 以 DQN/PPO 为主 |
| Q-learning | 离轨、最大化偏差 | DQN/Double DQN 论文 | `projects/vwxyzjn_cleanrl_en`；`projects/DLR_RM_stable_baselines3_en` |
| 函数逼近 | 投影、发散反例 | NDP 1996；REDQ；DrQ-v2 | CleanRL DQN/SAC |

## 策略优化

| 方法 | 资料 | 源码 |
|---|---|---|
| REINFORCE / VPG | Sutton 第 13 章；Spinning Up | `projects/openai_spinningup_en` |
| 自然梯度 / TRPO | `05_.../1502.05477`；1908.00261 | Spinning Up TRPO |
| PPO | `05_.../1707.06347` | CleanRL、SB3、Spinning Up |
| Actor–Critic / A3C | `05_.../1602.01783`；GAE | SB3 A2C；CleanRL |
| DDPG / TD3 | `04_.../1509.02971`；`05_.../1802.09477` | CleanRL、SB3、TorchRL |
| SAC / 最大熵 | `05_.../1801.01290` | 同上 |
| MPO | `05_.../1806.06920` | 本库未收官方 MPO 实现 |
| 连续动作 | 上述 + TorchRL | `projects/pytorch_rl_torchrl_en` |

Berkeley CS285 讲义：`courses/Berkeley_CS285_DeepRL_FA2023_en/`。  
Stanford CS234 Winter 2026：`courses/Stanford_CS234_ReinforcementLearning_W2026_en/`。  
欠驱动/DP/MPC 在线讲义：`courses/Tedrake_UnderactuatedRobotics_notes_html_en/`（覆盖范围见 `PAGES_en.txt`）。

## 有模型：规划与学习

| 方法 | 资料 | 源码/文档 |
|---|---|---|
| Dyna | Sutton 第 8 章；Silver 第 8 讲 | Silver 课件 `courses/` |
| MPC / 在线 lookahead | Bertsekas Lessons from AlphaZero；6.231 rollout | 控制课 `C-10` Tedrake 笔记（若已核验） |
| 世界模型 | DreamerV3、TD-MPC2、MuZero、EfficientZero 论文 `06_model_based/papers/` | 作者代码未全部收入；本库以论文+TorchRL 模块为主 |
| 模型误差 | Moerland 综述 `06_.../2006.16712` | — |

RLlib 文档（规划中的分布式训练）见 `software_docs/`（若本轮 HTML 核验通过）。

## 部分可观测

| 方法 | 资料 | 源码 |
|---|---|---|
| 信念 / 滤波 | Kochenderfer DMUU、ADM 第 19–22 章；Kaelbling 综述 | `projects/JuliaPOMDP_POMDPs_jl_en` |
| 记忆策略 | DRQN、递归无模型 RL 论文 `07_...` | CleanRL 无 DRQN 主文件；勿把 LSTM 包装当 POMDP 已解 |
| 近似求解 | Igl DVRL | POMDPs.jl 生态（SARSOP 等为独立包，本快照是接口） |

## 约束 / 风险 / 鲁棒

CPO、CVaR、Safe RL 综述、鲁棒综述：`08_constrained_risk_sensitive/papers/`。  
实现：`projects/Farama_Parkour_OmniSafe_en`（OmniSafe）。L1：看 `omnisafe/`、LICENSE、README。

## 离线学习与离策略评价

| 方法 | 论文 | 源码 |
|---|---|---|
| 问题设定 | Levine 2020 教程 | — |
| CQL | 2006.04779 | d3rlpy、CORL |
| IQL | 2110.06169 | 同上 |
| Decision Transformer | 2106.01345 | CORL |
| 双重稳健 OPE | Jiang & Li 1511.03722 | 论文算法；无单独官方大库 |
| 复现协议 | CORL 2210.07105 | `projects/tinkoff_CORL_en` |

## 多智能体 / 分层 / 博弈

MADDPG、QMIX、Option-Critic、MARL 综述、HRL 综述：`10_advanced_theory/papers/`。  
环境：`projects/Farama_PettingZoo_en`、`projects/deepmind_open_spiel_en`。

## 建议对照实验（建模完成后）

1. 小型有限 MDP：pymdptoolbox VI vs PI。  
2. 同一环境：已知模型 VI vs 未知模型 Q-learning（CleanRL DQN）。  
3. 离散 CartPole vs 连续 MuJoCo/Gymnasium 连续任务（SAC/TD3）。  
4. 部分可观测：全观测基线 vs 遮挡观测 + 递归策略。  
5. 约束：OmniSafe 与无约束 PPO。  
6. 离线：CORL 算法 + 论文中的 OPE。  

运行条件与指标见 `practical_cases_cn.md`。本轮不执行。
