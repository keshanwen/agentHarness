---
name: encoding-settings
description: 项目设置 UTF-8 编码，尝试使用 chcp 65001 设置命令行代码页
type: project
---

- `TEXT_ENCODING = "utf-8"` 用于文件读写。
- 调用 `os.system("chcp 65001")` 设置 Windows 命令行代码页为 UTF-8。
- 在当前 macOS 环境执行时输出 `sh: chcp: command not found`。
