# 实现与集成（静态核对）

可运行性：**L0** 已下载快照；**L1** 已核对入口、许可证、应有路径、SNAPSHOT。本轮不安装依赖、不运行、不部署、不接真实设备。

## 环境接口

路径：`projects/Farama_Gymnasium_en/`  
核对：`gymnasium/core.py`（`reset`/`step`、`terminated`/`truncated`）、`LICENSE`、`README.md`、`SNAPSHOT_en.txt`。  
文档离线集：`software_docs/Gymnasium_docs_html_en/`（覆盖范围见该目录 `PAGES_en.txt`：Env API、wrappers、vector、经典控制、CartPole、基本用法与自定义环境）。  
相关论文：Gymnasium 2407.17032。

多智能体：`projects/Farama_PettingZoo_en/`（AEC/Parallel）。  
博弈：`projects/deepmind_open_spiel_en/`。

## 算法参考实现

| 项目 | 路径 | 许可证（以仓库文件为准） | 入口 | 适用范围 |
|---|---|---|---|---|
| CleanRL | `projects/vwxyzjn_cleanrl_en/` | MIT | `cleanrl/` 单文件、README | 离散/连续无模型；实验配置清晰 |
| SB3 | `projects/DLR_RM_stable_baselines3_en/` | MIT | `stable_baselines3/` | 保存/加载、向量环境 |
| TorchRL | `projects/pytorch_rl_torchrl_en/` | 见 LICENSE | `torchrl/` | 可组合 collector/目标 |
| Spinning Up | `projects/openai_spinningup_en/` | MIT | `spinup/` | 教学；仓库已归档 |
| CORL | `projects/tinkoff_CORL_en/` | 见 LICENSE | `algorithms/` | 离线；**无 D4RL 数据** |
| d3rlpy | `projects/takuseno_d3rlpy_en/` | MIT | `d3rlpy/` | 离线 API |
| OmniSafe | `projects/Farama_Parkour_OmniSafe_en/` | 见 LICENSE | `omnisafe/` | 约束/安全 |
| pymdptoolbox | `projects/sawcordwell_pymdptoolbox_en/` | LICENSE.txt | README.rst | 表格 VI/PI |
| POMDPs.jl | `projects/JuliaPOMDP_POMDPs_jl_en/` | LICENSE.md | `src/` | 接口；求解器另包 |
| ADM 配套 | `projects/algorithmsbooks_decisionmaking_en/` | 可能仅 README | README | 与 B-02 配套；文件少则记为部分 |

每个目录含 `SNAPSHOT_en.txt`：repo、ref、commit、归档哈希。

RLlib：**不收 Ray 源码**（体积）。文档子集：`software_docs/RLlib_docs_html_en/`（`PAGES_en.txt`）。

其他官方文档离线集（均有 `PAGES_en.txt`）：`software_docs/StableBaselines3_docs_html_en/`、`software_docs/CleanRL_docs_html_en/`、`software_docs/TorchRL_docs_html_en/`、`software_docs/PettingZoo_docs_html_en/`、`software_docs/d3rlpy_docs_html_en/`。

## 测试、配置、评测、日志、保存

- **测试**：SB3/Gymnasium/CleanRL 仓库内 `tests/` 或 CI 说明；本轮未执行。  
- **配置**：CleanRL 命令行；CORL yaml；SB3 构造函数。  
- **评测**：关探索、独立种子、多次回合。  
- **日志**：CleanRL 可接实验跟踪；本快照不含 wandb 缓存。  
- **保存/加载**：SB3 `save`/`load`；文档页。权重文件已按规则丢弃 `*.pt/*.pth`。

## 缺失外部资源（如实）

- 大型数据集（D4RL、Atari ROM、MuJoCo 许可模型）未下载。  
- 训练权重未保存。  
- OpenSpiel 游戏资源若走 LFS，SNAPSHOT 会注明；本轮核验写明未见 LFS 指针则仅指快照内。  
- `algorithmsbooks_decisionmaking` 快照文件数很少，算法正文可能在教材 PDF/其他仓库。  
- hiive/mdptoolbox 需登录，未收入。

## 决策系统集成（只谈接口，不部署）

推荐边界：

1. 环境实现 Gymnasium `Env`：动作/观测空间、`terminated`/`truncated` 语义。  
2. 策略模块：`predict(obs) -> action`；训练循环不进入生产进程。  
3. 安全：约束检查在环境或包装器，不信任奖励整形。  
4. 日志：决策时刻只用当时可得信息。  
5. 版本：记录 Gymnasium 与算法 commit（SNAPSHOT）。

后续真要跑：新建隔离环境，按 SNAPSHOT 与 README 安装；禁止把上游 README 数字当本机复现。

下一步：`guides/core_reading_list_cn.md`。
