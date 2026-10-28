# LeanCapsule 工件格式

每个 capsule 目录至少包含：

- `Capsule.lean`：可直接编译的完整文件或抽取后的文件；
- `capsule.json`：目标、环境、期望诊断、来源和回放命令；
- `expected-diagnostic.txt`：原始编译输出，供人工审计；
- `lean-toolchain`、`lakefile.toml`、`lake-manifest.json`：存在时复制；
- `replay.ps1`、`replay.sh`：跨平台回放脚本；
- `README.md`：面向读者的简短说明。

## 诊断比较

`diagnostic_key` 由诊断类别和规范化核心消息组成。规范化会去除临时路径、行列号、连续空白以及不稳定的 metavariable 编号。回放通过必须同时满足：

1. 编译成功/失败状态一致；
2. 诊断类别一致；
3. `diagnostic_key` 文本一致。

原始输出不会被替换，因而可以在人工复核时追踪编译器实际反馈。

写入公开工件前会保留错误正文并将绝对本机路径替换为稳定占位文本。运行 `python -m leancapsule audit capsules` 可检查公开目录是否仍含本机路径、疑似敏感凭据或不完整的成功证明。

## 来源与许可

公开 capsule 必须补充来源、许可、Lean 工具链和已知限制。生成命令只提供占位 provenance，发布前需要人工完善。
