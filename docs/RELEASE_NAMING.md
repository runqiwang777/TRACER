# v3 公开命名与既有运行

本公开版本统一使用 **v3** 标识当前研究阶段。文档、Python 入口、PowerShell 脚本、配置文件路径、协议标识和进程内密钥变量使用同一命名，不以投稿目标命名。

## 入口

| 用途 | 当前入口 |
| --- | --- |
| 离线审计 | `python src/v3.py audit` |
| 合成连接预检 | `scripts/preflight_v3.ps1` |
| 正式运行与续跑 | `scripts/run_v3_formal.ps1` |
| 执行协议 | [V3_EXPERIMENT_PROTOCOL.md](V3_EXPERIMENT_PROTOCOL.md) |
| 科学协议 | `experiments/preregistrations/tracer_protocol_v3.json` |
| 扩展配置 | `experiments/causal_feedback.tracer_extended_v3.json` |
| 确认配置 | `experiments/causal_feedback.tracer_minimax_confirmatory_v3.json` |

预检和正式脚本在本进程中使用 `TRACER_V3_DEEPSEEK_KEY`、`TRACER_V3_GLM_KEY`、`TRACER_V3_MINIMAX_KEY`，退出时清理。不要把密钥写入源码或公开记录。

## 研究可比性

此次是公开名称调整，不是新实验或重新预注册。冻结日期、题目、项目划分、模型、采样参数、提示文件、随机顺序、请求预算、停止规则和分析方法保持原值。历史 v2 配置仍保留其版本号，用于兼容与协议追溯；不将其改称 v3 结果。

## 既有批次

既有本机输出目录、原始日志及预注册原件不在这次公开重命名中改写。旧批次继续使用与其冻结配置匹配的原工作副本、原运行脚本和原输出目录。不要把本公开版配置或重命名后的协议直接替换进旧运行根目录；续跑会检查完整配置与协议，名称变化也可能导致拒绝。

从本公开版本启动的新批次使用 `results/v3-formal-日期-随机后缀/`。只有运行时合同及配置匹配时，才能通过 `-Resume -RunRoot` 恢复。公开命名调整不授权重新调用已完成的付费任务，也不把新批次与旧批次合并。

本次仅更新当前文件树；Git 历史及本机原始证据不在本次改写范围内。
