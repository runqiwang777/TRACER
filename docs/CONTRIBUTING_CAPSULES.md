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
