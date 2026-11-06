# MDP 建模指南

把业务写成 MDP 时，先写清元组，再选算法。本库案例见 `practical_cases_cn.md`。

## 必须写下来的字段

| 字段 | 含义 | 常见失败 |
|---|---|---|
| 状态 \(S\) | 决策所需充分统计 | 漏掉会破坏马尔科夫性的变量 |
| 动作 \(A\) | 决策者真实可控量 | 把不可执行的“期望产量”当成动作 |
| 转移 \(P\) | \(s'|s,a\)，已知或未知 | 用未来信息拟合 \(P\) |
| 奖励 \(R\) | 与业务目标一致的标量/向量 | 优化了代理指标，业务指标不动 |
| 时域 | 有限 / 无限 / 不定长 | 把截断当终止 |
| 折扣 \(\gamma\) 或平均奖励 | 准则 | 平均奖励问题却用 \(\gamma=0.99\) 不声明 |
| 约束 | 安全、预算、CVaR | 只在奖励里罚一下，可行性无保证 |
| 观测 | 全观测或 POMDP | 观测混叠仍当 MDP |
| 数据 | 在线交互 / 离线日志 | 日志策略覆盖不足仍学贪心 |

## 马尔科夫假设

合理：状态已包含影响下一转移与奖励的历史充分统计（库存量、机器退化等级、电网节点状态等）。  
不合理：用部分传感器读数当状态、却依赖未写入状态的班次/天气/设备编号。此时应：扩充状态、改 POMDP/信念、或加记忆策略（见 `07_partial_observability/papers/`）。

## 奖励与业务目标

- 库存：持有+缺货成本，是否包含服务水平约束（应进约束而非只进奖励）。  
- 维护：故障损失 vs 计划停机；若业务要“不停机”，罚函数可能仍产出停机策略。  
- 医疗：短期实验室指标 vs 长期预后；离线电子病历有混杂。  
应用综述：`11_applications/papers/`。仿真变好 ≠ 现场有效。

## 终止、截断与自举

Gymnasium 把 `terminated` 与 `truncated` 分开（论文 `12_software_practice/papers/` Gymnasium；文档预定 `software_docs/`）：

- **terminated**：进入终止状态（吸收、任务成功/失败）。价值目标里 bootstrap **停止**。  
- **truncated**：到时限、外部打断。状态仍可能有后续价值，bootstrap **继续**（用 \(V(s')\)）。  

混用会导致有限时域偏差。Sutton 书中“episode 结束”在工程里必须拆成这两类。

## 已知模型 vs 未知模型

| | 已知 \(P,R\) | 未知 |
|---|---|---|
| 工具 | `projects/sawcordwell_pymdptoolbox_en`、`projects/algorithmsbooks_decisionmaking_en`、6.231 讲义 | CleanRL / SB3 / TorchRL |
| 方法 | VI / PI / LP | TD、Q、策略梯度、有模型学习 |
| 风险 | 模型误差当真理 | 探索不足、非平稳 |

Bertsekas《Lessons from AlphaZero》把离线训练与在线 lookahead/MPC 分开写，适合“有粗模型再在线修正”。

## 约束与风险

CMDP、拉格朗日、CVaR、鲁棒转移：论文 `08_constrained_risk_sensitive/papers/`，代码 `projects/Farama_Parkour_OmniSafe_en`。  
可行性：先检查约束可满足，再谈平均回报。Boyd / Bertsekas 凸对偶是拉格朗日法的先修。

## 离线数据

覆盖、离策略偏差、OOD 动作：`09_offline_evaluation/papers/` 与 `projects/tinkoff_CORL_en`、`projects/takuseno_d3rlpy_en`。  
没有覆盖的动作上的高 Q 值不可信（CQL 的动机）。

## 未来信息

禁止：用 \(t+1\) 才知道的需求/故障标签当 \(t\) 的状态；用测试集轨迹调奖励。  
允许：因果上在决策前可观测的预报（并写入状态定义）。

下一步：`guides/practical_cases_cn.md`、`guides/evaluation_pitfalls_cn.md`。
