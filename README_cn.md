# 马尔科夫决策过程与序贯决策资源库

独立目录：`/root/markov_decision_process_resources/`。检索日 **2026-10-30**。论文五年窗口 **2021-10-30 至 2026-10-30**；必要奠基论文单列。教材允许经典版本。

本轮只收集整理：不安装依赖、不运行实验、不控制真实设备、不部署、不上传 GitHub、不删除资料。完成后停止，不进入独立 Monte Carlo 方法库或 EM 专题。

## 子方向

| 目录 | 内容 |
|---|---|
| `01_foundations/` | 条件概率、条件期望、马尔科夫链、随机过程、线性代数、优化与 DP 基础 |
| `02_mdp_core/` | 状态、动作、转移、奖励、策略、轨迹、价值函数；时域、折扣、平均奖励、占用测度 |
| `03_dynamic_programming/` | Bellman 方程、策略评估/迭代、价值迭代、收敛、LP、近似 DP |
| `04_model_free_learning/` | MC 评估、TD、SARSA、Q-learning、资格迹、探索、函数逼近（不为独立 MC 库） |
| `05_policy_optimization/` | 策略梯度、Actor–Critic、自然梯度、信赖域、最大熵、连续动作 |
| `06_model_based/` | 转移估计、规划与学习、Dyna、MPC 联系、模型误差 |
| `07_partial_observability/` | POMDP、信念、滤波、记忆策略、观测混叠 |
| `08_constrained_risk_sensitive/` | 约束 MDP、拉格朗日、风险/CVaR、鲁棒、安全约束 |
| `09_offline_evaluation/` | 离线 RL、OPE、重要性采样、双重稳健、覆盖与 OOD |
| `10_advanced_theory/` | 随机最短路、随机博弈、分层、半马尔科夫、连续状态 |
| `11_applications/` | 机器人与控制、维护、调度、库存、能源、交通、医疗；区分模拟与现场 |
| `12_software_practice/` | 环境接口、参考实现、测试、配置、评测、日志、保存加载 |

论文在各目录 `papers/`。教材、课程、软件文档、项目分别在 `books/`、`courses/`、`software_docs/`、`projects/`。

## 登记文件

- `catalog_cn.csv` 已核验条目
- `progress_cn.csv` 分方向进度
- `download_failures_cn.csv` 失败与待核验
- `project_readiness_cn.csv` 代码 L0/L1（本轮不执行）
- `search_log_cn.md` 检索与复用说明
- `guides/` 学习与工程路线（中文）

独立自建文件在扩展名前标 `_cn` 或 `_en`。上游源码内部文件名保持原样；外层归档包添加语言后缀。

## 指南（三条路线）

理论：`guides/foundations_path_cn.md`、`guides/mdp_modeling_guide_cn.md`、`guides/core_reading_list_cn.md`  
算法实现：`guides/algorithms_map_cn.md`、`guides/implementation_integration_cn.md`  
应用建模：`guides/practical_cases_cn.md`、`guides/evaluation_pitfalls_cn.md`

## 完整性规则（摘要）

只计核验通过的完整资料。PDF 须可解析且正文完整。摘要/试读/残章不计。分章节教材完整后整本计一次。课程按完整资料包计。HTML 保存为离线页并记录 `PAGES_en.txt` 覆盖范围。源码保留结构、许可证、`SNAPSHOT_en.txt`（含 commit）。不下载大数据集、训练权重、安装包。不绕过付费墙。不额外做整库哈希扫描。

## 代码等级

- **L0**：已下载快照。
- **L1**：静态见到 README、许可证、依赖清单、SNAPSHOT、应有入口。
- 本轮不运行，不声称复现或可用于生产。

## 断点续跑

```bash
cd /root/markov_decision_process_resources
python3 -I scripts/materials_en.py status
python3 -I scripts/papers_en.py status
python3 -I scripts/materials_en.py fetch books --retry-failed
python3 -I scripts/materials_en.py fetch courses --retry-failed
python3 -I scripts/materials_en.py fetch software --retry-failed
python3 -I scripts/materials_en.py fetch projects --retry-failed
python3 -I scripts/papers_en.py download NN --retry-failed   # NN = 01..12
python3 -I scripts/build_catalog_en.py
```

已核验条目不会覆盖。工作缓存：`/root/.cache/mdp_lit/`。arXiv 与兄弟文献库共享 `arxiv.org` 锁。

## 明确未收入（合法全文不可得或不在本轮范围）

- Puterman《Markov Decision Processes》全书、Altman《Constrained MDPs》全书：无合法免费全文。
- 商业 RL 书扫描版。
- Ray/RLlib 源码单体（体积）；仅收官方文档子集（若核验通过）。
- D4RL 等大型离线数据集、Atari ROM、MuJoCo 许可模型、训练权重。
- 独立 Monte Carlo 数值方法库、EM 算法专题。
