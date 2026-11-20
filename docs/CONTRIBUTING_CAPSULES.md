# Capsule 贡献说明

提交新 capsule 前，请确保：

1. 输入文件不含密钥、个人路径或隐私数据；
2. `python -m leancapsule replay <目录>` 在干净环境中通过；
3. manifest 中的来源、许可、工具链和预期诊断完整；
4. README 能说明错误现象和回放方法；
5. 不把成功的 `sorry` 题目伪装成真实失败案例；
6. 同时运行 Python 测试和 `lake build`。
7. 运行 `python -m leancapsule audit capsules`，确保发布审计通过。

贡献者应说明 capsule 是 standalone 还是 full-file fallback，并报告已知的跨平台限制。


## 环境检查 FAQ

提交或复核 capsule 前，先用以下检查排除 Lean/Lake 环境问题（不需要 API key，也不会产生付费模型调用）：

1. **确认工具链版本**：运行 `elan show`，核对输出与 capsule 的 `lean-toolchain` 文件一致。
2. **确认 `lake` 可用**：运行 `lake --version`；若命令不存在，请按 [CONTRIBUTING](../CONTRIBUTING.md) 第 1 条重装 Lean/Lake。
3. **`lake build` 无法下载依赖**：先检查网络与代理设置，然后重试 `lake build`；仍失败时保留完整错误输出并联系维护者。

这些检查只覆盖环境/安装问题；证明失败请参考 [CAPSULE_FORMAT.md](CAPSULE_FORMAT.md) 的诊断比较，模型接入问题请参考 API 文档。相关术语见 [CAPSULE_FORMAT.md 术语表](CAPSULE_FORMAT.md#术语表)。
