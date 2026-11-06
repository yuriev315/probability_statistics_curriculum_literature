# 检索日志

检索日：2026-10-30。五年窗口：2021-10-30 至 2026-10-30。经典论文单列。

## 已有资料库核查

| 资料库 | 路径 | 结果 |
|---|---|---|
| 信号处理文献库 | `/root/signal_processing_literature` | 存在。复用 Boyd & Vandenberghe《Convex Optimization》全文 PDF（本库重新核验）。 |
| 近期顶会研究 | `/root/recent_top_conference_research` | 存在。以时间序列/机器人为主，本轮未移动原件；论文按 arXiv 新下为主。 |
| 高斯过程 / 概率统计课程 / AI 课程 / 控制 / 机器人 / 时间序列 / 工业过程监控 | `/root/gaussian_process_literature` 等 | 本机目录不在；仅见 `/root/.cache/*_lit` 工作缓存。本轮无法复制原件。 |

规则：不移动原件、不重复计数；复用项在本库重新核验。

## 检索渠道

- 论文：arXiv API 元数据核验后再下载 PDF；作者/学会开放获取 PDF（JAIR、JMLR、MDPI、作者站点）。
- 教材：作者站点免费全书（incompleteideas.net、MIT Bertsekas、algorithmsbook/Google Drive 官方全书、AMS/CUP 作者 PDF、Stanford SISL）。
- 课程：MIT OCW 官方课件包、UCL Silver 教学页、Berkeley CS285 公开讲义、Stanford CS234 课程页、Spinning Up / Hugging Face 公开教程。
- 软件：官方 HTML 文档子集。
- 项目：GitHub 官方仓库 zip 快照；丢弃权重与大型数据。

不绕过付费墙；不下载商业软件本体、破解工具或付费手册。Puterman《Markov Decision Processes》、Altman《Constrained MDPs》等商业书未计入（无合法全文）。

## 论文筛选

- 先列候选 arXiv ID，用 API 核对标题后再入库；错误 ID（主题不符）已剔除，不下载。
- 近五年优先 ICML/NeurIPS/ICLR 及 UAI/AISTATS/CoRL 等；经典单列并填写保留理由。
- 渠道按实际标注（arXiv 预印本、期刊开放获取、会议主会），不宣称所有渠道同级。

## 工具与代码

检索并选择互补项目：Gymnasium、Stable-Baselines3、CleanRL、TorchRL（文档+源码）、RLlib（仅文档，源码随 Ray 过大）、OpenSpiel、PettingZoo、d3rlpy、CORL、pymdptoolbox/hiive、POMDPs.jl、Spinning Up、OmniSafe、教材配套 Julia 代码。

## 失败与缺口（随下载更新）

见 `download_failures_cn.csv`。扫描版无文字层的作者 PDF（如部分 Athena 重印）不计入完整资料。

已知缺口（不计数）：

- B-10 Bertsekas *Stochastic Optimal Control: The Discrete-Time Case*、B-15 *Constrained Optimization and Lagrange Multiplier Methods*：Athena 扫描 PDF 前 12 页抽不出名称短语，不计入。
- C-08 Hugging Face Deep RL Course：索引链接落到 `.md`（`text/markdown`），HTML 核验规则拒绝，不计入。课程目标已由 8 套其他完整课包覆盖。
- C-09 CMU 托管 Sutton 教材副本：与 B-01 同源，种子已 `exclude`，不重复计数。
- P-13 hiive/mdptoolbox：`git ls-remote` 需登录，已排除；精确 DP 用 pymdptoolbox。
- Puterman、Altman 全书：无合法免费全文。
- RLlib 源码：随 Ray 体积过大，只收文档子集。
- 大型数据集与权重：按规则不下载。

## 课程与文档抓取调整

- MIT OCW 使用官方 zip（6.041SC、18.06、6.231），不再用已失效的 `static_resources` PDF 正则。
- Silver 课件跳过作业/考试短 PDF。
- CS234 改为 Winter 2026 `/slides/lecture*post.pdf` 完整课件包（754 页）。
- Tedrake 在线讲义按章节 HTML 子集保存（`PAGES_en.txt`）。
- Gymnasium 文档正则收窄到 API/经典控制/入门，避免镜像全部 MuJoCo/Atari 环境页。

## 代码快照

官方 GitHub zip 按 commit 固化，见各 `projects/*/SNAPSHOT_en.txt`。丢弃 `*.pt/*.pth` 等权重。P-12 `algorithmsbooks/decisionmaking` 仅 2 个文件，记为 L0 部分配套。

官方文档 7 套均已核验：Gymnasium、SB3、CleanRL、TorchRL、RLlib、PettingZoo、d3rlpy。覆盖范围见各目录 `PAGES_en.txt`。

## 本轮核验计数（只计完整通过）

| 类型 | 已核验 | 目标 | 新下载 | 复用 |
|---|---|---|---|---|
| 教材/专著 | 15 | 10–20 | 14 | 1（Boyd，来自 signal_processing_literature） |
| 大学课程/讲义/系统教程 | 8 | 8–12 | 8 | 0 |
| 论文/综述/教程 | 57 | 约 50 | 57 | 0 |
| 其中近五年窗口 | 13 | 优先近五年 | — | — |
| 其中窗口前（含经典补充） | 44 | 奠基单列 | — | — |
| 官方工具文档 | 7 | 5–8 | 7 | 0 |
| 算法实现/实践项目 | 13 | 10–15 | 13 | 0（P-12 为 L0） |

目录合计 100 条。失败不计数：B-10、B-15、C-08。去重：C-09 与 B-01 同源已排除；hiive/mdptoolbox 排除。不重复计数原库 Boyd，仅本库复检后计 1 次。

