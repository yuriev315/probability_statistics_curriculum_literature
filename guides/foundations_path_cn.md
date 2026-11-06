# 理论学习路线

检索日 2026-10-30。只使用本库已核验资料。本轮未运行代码。

## 路线目标

建立：条件概率与条件期望 → 马尔科夫链 → 有限 MDP 与价值函数 → Bellman 算子与动态规划 → 无模型预测/控制的数学图像。不进入独立 Monte Carlo 方法库或 EM 专题。

## 第 0 段：概率与线性代数（约 1–2 周）

1. 课程包 `courses/MIT_OCW_6_041SC_ProbabilisticSystems_F2013_en.zip`（Tsitsiklis，MIT OCW 6.041SC）  
   条件概率、条件期望、贝叶斯。对应 MDP 中的 \(P(s'|s,a)\) 与 \(v^\pi(s)=\mathbb{E}[G_t|S_t=s]\)。
2. 课程包 `courses/MIT_OCW_18_06_LinearAlgebra_S2010_en.zip`（Strang）  
   矩阵、特征分解、最小二乘。对应占用测度线性方程、线性价值逼近。
3. 教材 `books/BoydVandenberghe_ConvexOptimization_2004_en.pdf`（复用自 signal_processing_literature B-14，本库复检）  
   对偶与约束，后面约束 MDP 拉格朗日方法要用。
4. 教材 `books/Bertsekas_ConvexOptimizationTheory_2009_en.pdf`  
   比 Boyd 更偏对偶几何，可选。

## 第 1 段：马尔科夫链（约 1 周）

1. `books/LevinPeresWilmer_MarkovChainsMixingTimes_2e_en.pdf`  
   有限链、平稳分布、总变差、混合时间。重点：不可约/非周期、可逆性。  
   注意：混合时间服务于采样，不是 MDP 求解本身；用来判断“轨迹是否像平稳占用”。
2. 对照 `books/SuttonBarto_ReinforcementLearning_2e_2020_en.pdf` 第 2–3 章的随机过程语言。

## 第 2 段：MDP 核心对象（约 2 周）

主教材（按这一顺序，不要并行读三本全书）：

1. Sutton & Barto 第 3–4 章：状态、动作、转移、奖励、策略、轨迹、\(v_\pi,q_\pi\)，有限时域直觉。  
   对照：`courses/Stanford_CS234_ReinforcementLearning_W2026_en/`（Winter 2026 课后讲义）。  
2. `books/KochenderferWheelerWray_AlgorithmsForDecisionMaking_2022_en.pdf` 第 7 章前后：精确求解、折扣。  
3. `books/Szepesvari_AlgorithmsForReinforcementLearning_2010_en.pdf` 第 2 章：把 MDP 写成 DP 对象。

论文：

- `01_foundations/papers/1988_Sutton_LearningPredictMethods_en.pdf`：条件期望与 TD。  
- `02_mdp_core/papers/` DualDICE、平均奖励 OPE：占用测度与折扣/平均奖励两种准则。

必做辨析（写在笔记里）：

- 马尔科夫假设是否对你的业务状态成立。  
- 折扣 \(\gamma\)、平均奖励、有限期：三者不可混用同一套 Bellman 方程。  
- 终止：目标达成 vs 时间截断（见实践指南）。

## 第 3 段：动态规划与收敛（约 2 周）

1. 课程包 `courses/MIT_OCW_6_231_DynamicProgramming_F2015_en.zip`（Bertsekas 6.231）讲义全本。  
2. `books/Bertsekas_AbstractDynamicProgramming_3e_2022_en.pdf`：Bellman 算子收缩/非收缩。  
3. `books/Bertsekas_ACourseInReinforcementLearning_2e_2025_en.pdf`：价值空间近似与牛顿法视角。  
4. `books/BertsekasTsitsiklis_NeuroDynamicProgramming_1996_en.pdf`：函数逼近失败模式（反例）。  
5. 论文 `03_dynamic_programming/papers/` rollout 与 Li 2017 概览。

算法对应：策略评估 → 策略迭代 → 价值迭代；误差界来自压缩映射，不是来自一次仿真曲线。

## 第 4 段：无模型学习（只到理解 MDP 学习为止）

Sutton & Barto 第 5–12 章 + `04_model_free_learning/papers/`（DQN、Double DQN、REDQ、DrQ-v2、DDPG）。  
Monte Carlo **策略评估**只作为“无自举、有终止”的对照，不扩展成独立抽样方法库。

资格迹：Sutton 第 12 章与 GAE 论文（`03_dynamic_programming/papers/` 中的 1506.02438）。

## 第 5 段：研究生理论专题（选修）

- `books/AgarwalBrantleyJiangKakadeSun_RLTheoryAndAlgorithms_2026_en.pdf`（工作草稿，日期以扉页为准）  
- `01_foundations/papers/` 线性函数逼近可证明效率、策略梯度理论  
- `books/LattimoreSzepesvari_BanditAlgorithms_2020_en.pdf`：探索下界，再回到有状态 MDP

## 三条路线如何分流

| 路线 | 读到哪里转入 |
|---|---|
| 理论 | 本文件第 3–5 段 → `algorithms_map_cn.md` 的收敛/复杂度 |
| 算法实现 | 第 2–4 段后转 `algorithms_map_cn.md` + `implementation_integration_cn.md` |
| 应用建模 | 第 2 段后转 `mdp_modeling_guide_cn.md` + `practical_cases_cn.md` |

下一步：`guides/algorithms_map_cn.md`。
