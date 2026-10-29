# 当前研究协议

当前付费修复研究以 v3 因果实验协议 v3 为准。本仓库不包含早期 repair24 六臂付费批次的完整轨迹、证明和人工/AI 复核账本，因此其历史聚合结果不作为当前可审计结果。

## 冻结题库与条件

- 基准：TRACER-REAL v2 的五个独立 test 项目、254 道修复任务。
- 重复：每模型、每题三次。
- 确认条件：`content_free_retry`、`true_structured`、`counterfactual`。
- 扩展条件：再加入 `raw`、`normalized`、`irrelevant`、`retrieval_only`、`adaptive`。
- 嵌套：DeepSeek 和 GLM 运行八个条件；MiniMax 只运行三个确认条件。
- 主要配对：同模型、同题、同重复、同一个冻结首轮失败下，比较 `true_structured` 与 `content_free_retry`。

安全策略使用独立的 SP-n 编号，不能作为修复实验条件合并分析。

## 执行与门禁

实验协议、三家模型配置、预注册与可续跑脚本见 [v3 执行协议](V3_EXPERIMENT_PROTOCOL.md)。在密钥提示前先运行离线审计与合成定理预检；正式批次使用独立输出目录，网络中断后沿原目录续跑。完成后必须通过轨迹校验、成功证明独立复编译、AI 辅助复核和脱敏发布审计。

当前没有可用于研究结论的完整付费批次。任务上限、预注册或预检通过都不是实验结果。
