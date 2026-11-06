# 核心阅读清单

只列本库已核验全文。顺序按三条路线。论文近五年与经典分开。

## 理论路线（约 8–12 周）

1. 6.041SC 概率课包 → Levin 混合时间选读第 1–4 章  
2. Sutton & Barto 2e（2020 印）第 3–4 章  
3. Szepesvári《Algorithms for RL》第 1–2 章  
4. 6.231 DP 课包 + Abstract DP 3e 收缩映射章节  
5. 1988 Sutton TD；1907.05388 线性函数逼近；1908.00261 策略梯度理论  
6. Agarwal 等 RL Theory 草稿（扉页日期 2026-06-27，工作草稿）  
7. DualDICE；平均奖励 OPE；Jiang & Li 双重稳健  

## 算法实现路线

1. Sutton 第 5–13 章（MC 评估、TD、资格迹、策略梯度）  
2. Silver 课件十讲（`courses/UCL_Silver_ReinforcementLearning_2015_en/`）  
3. CS285 Fall 2023 讲义；CS234 Winter 2026 课后讲义  
4. DQN → Double DQN → DDPG → TD3 → SAC → PPO → TRPO  
5. Moerland MBRL 综述；MuZero；DreamerV3 或 TD-MPC2 择一深读  
6. Gymnasium 论文 + CleanRL 论文 + 对应源码入口  
7. 离线：Levine 教程 → CQL → IQL → CORL  

实现时对着 `algorithms_map_cn.md` 打开 L0 源码，不运行。

## 应用建模路线

1. ADM（Kochenderfer et al. 2022）第 7、16–22 章：精确求解、模型不确定、信念  
2. DMUU（2015）应用章：碰撞回避等，区分理论与任务  
3. `mdp_modeling_guide_cn.md` 填表  
4. 应用论文四篇（医疗、库存、交通、OR 综述）——每篇标注模拟/回顾/现场  
5. 约束：CPO + Safe RL 综述；风险：CVaR 论文  
6. 维护/库存：用 pymdptoolbox 先做表格模型，再考虑学习  
7. 控制侧 DP/MPC：`courses/Tedrake_UnderactuatedRobotics_notes_html_en/`  

## 经典（窗口前）必读

Sutton 1988；Kaelbling et al. JAIR 1996；NDP 1996；DQN；TRPO；PPO；SAC；CPO；Jiang & Li 2016；Levine 离线教程 2020。

## 近五年（2021-10-30 起）优先

IQL、Decision Transformer、DreamerV3、TD-MPC2、EfficientZero、Safe RL 综述（2022）、离线综述 Prudencio、CORL、Gymnasium、TorchRL、CleanRL、CS285 2023、RL Theory 草稿更新。

## 不读/未收（避免误会）

- Puterman 全书、Altman CMDP 全书：无合法免费全文，不计入。  
- 商业 RL 书扫描版：不收。  
- 独立 Monte Carlo 数值积分专题、EM 算法专题：本轮不做。  

完整书目与路径：`catalog_cn.csv`。
