# 人工智能本科—研究生课程资料库

按 20 个主题整理的人工智能课程资料，覆盖从数学基础到大模型、具身智能和可信人工智能：教材、课程讲义包、论文、实践代码和培养方案参考，共 367 个条目。
有开放许可的文件（2.01 GiB）放在 Release `ai-curriculum-20261106` 的附件里，其余条目提供指向官方页面的 `.url` 链接。

## 内容

| 类型 | 合计 | 公开文件 | 占位链接（版权受限） | 占位链接（超过 100 MiB） | 占位链接（未取得） | 占位链接（无整包下载） | 网页链接 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 教材 | 53 | 24 | 22 | 1 | 6 | 0 | 0 |
| 课程 | 38 | 31 | 0 | 5 | 0 | 2 | 0 |
| 论文 | 225 | 88 | 137 | 0 | 0 | 0 | 0 |
| 实践 | 30 | 23 | 1 | 6 | 0 | 0 | 0 |
| 培养方案 | 21 | 0 | 14 | 0 | 0 | 0 | 7 |
| 合计 | 367 | 166 | 174 | 12 | 6 | 2 | 7 |

## 下载与解压

1. 在 Release `ai-curriculum-20261106` 下载全部 `ai_curriculum_20261106_batch*_cn_en.tar`。
2. 把它们解压到同一个目录，例如 `tar -xf ai_curriculum_20261106_batch001_cn_en.tar`（Windows 可用 7-Zip 或系统自带的 `tar`）。
3. 用 `SHA256SUMS.txt` 校验附件；解压后每个文件的 SHA-256 在 `archive_index_cn.csv` 和 `catalog_cn.csv` 中。

本分支只包含说明、目录和全部 `.url` 文件，不含 PDF 和 zip。

## 目录结构

| 目录 | 内容 |
|---|---|
| `books/<主题>/` | 教材和讲义 PDF |
| `courses/<主题>/` | MIT OpenCourseWare 课程整包（zip，含讲义、作业与考试） |
| `papers/<主题>/` | 论文 PDF，文件名以 arXiv 编号开头 |
| `practice/<主题>/` | GitHub 仓库在固定提交上的源码快照 |
| `curricula/` | 课程标准和培养方案参考 |
| `guides/` | 学习路径与清单 |

| 编号 | 目录名 | 主题 | 条目 |
|---|---|---|--:|
| 01 | `01_math_foundations` | 数学基础 | 19 |
| 02 | `02_probability_statistics` | 概率与统计 | 17 |
| 03 | `03_optimization_information_theory` | 最优化与信息论 | 17 |
| 04 | `04_cs_programming_foundations` | 计算机与编程基础 | 18 |
| 05 | `05_ai_foundations` | 人工智能基础 | 12 |
| 06 | `06_machine_learning` | 机器学习 | 19 |
| 07 | `07_deep_learning` | 深度学习 | 21 |
| 08 | `08_probabilistic_graphical_models` | 概率图模型与近似推断 | 10 |
| 09 | `09_natural_language_processing` | 自然语言处理 | 13 |
| 10 | `10_llm_agents` | 大语言模型与智能体 | 18 |
| 11 | `11_computer_vision` | 计算机视觉 | 16 |
| 12 | `12_generative_multimodal` | 生成模型与多模态 | 16 |
| 13 | `13_reinforcement_learning_control` | 强化学习与控制 | 24 |
| 14 | `14_robotics_embodied_ai` | 机器人与具身智能 | 20 |
| 15 | `15_time_series_signal_processing` | 时间序列与信号处理 | 18 |
| 16 | `16_graph_learning_recommender` | 图学习与推荐系统 | 20 |
| 17 | `17_causal_inference_sciml` | 因果推断与科学机器学习 | 19 |
| 18 | `18_trustworthy_ai` | 可信人工智能 | 22 |
| 19 | `19_ai_systems_deployment` | 人工智能系统与部署 | 18 |
| 20 | `20_research_methods_practice` | 研究方法与实践 | 9 |

## 指南

- `guides/curriculum_map_cn.md`：20 个主题、建议阶段和条目数量
- `guides/undergraduate_path_cn.md`：本科学习路径
- `guides/graduate_path_cn.md`：研究生学习路径
- `guides/core_reading_list_cn.md`：各主题核心论文
- `guides/practice_projects_cn.md`：实践材料
- `guides/engineering_path_cn.md`：工程实践路径

## 文件说明

- `catalog_cn.csv`：全部条目，含来源、许可、许可依据、库内路径和 SHA-256
- `release_excluded_cn.csv`：只提供 `.url` 的条目及原因
- `archive_index_cn.csv`：每个文件所在的附件、大小和 SHA-256
- `.url`：Windows 可直接双击打开，也可以用文本编辑器查看其中的地址和说明

## 许可

只有找到明确再分发许可的文件才放进附件：CC 系列（包括 NC、ND）、GFDL、公有领域，以及 MIT、Apache-2.0 等开源许可。各文件保留其上游许可，NC、ND 等限制仍然有效，使用前请查看 `catalog_cn.csv` 中的许可和许可依据。

arXiv 默认许可（非独占分发许可）、仅限个人使用、保留所有权利或未声明许可的材料只提供链接。超过 100 MiB 的文件也只提供链接。

如果你是权利人并希望移除某个文件，请提 Issue。
