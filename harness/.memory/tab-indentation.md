---
name: tab-indentation
description: 用户偏好使用 Tab 键缩进代码，而不是空格
type: feedback
---

# 缩进偏好：Tab

用户明确表示：**更喜欢用 Tab 键缩进，而不是空格**。

## 应用方式
- 写新代码 / 新建文件时，缩进一律使用 Tab 字符（`	`）。
- 修改已有文件时，跟随该文件既有的缩进风格，不要混用；如需重排缩进，优先改成 Tab。
- 生成配置（例如 .editorconfig）时使用 `indent_style = tab`。
- 不要擅自把用户代码里的 Tab 替换成空格。

