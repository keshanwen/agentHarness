---
name: skill-frontmatter-parsing
description: SKILL.md 使用 YAML frontmatter，由 --- 包裹，解析为 meta 和正文
type: project
---

`parse_frontmatter(text)` 检查文本是否以 `---` 开头；用 `text.split("---", 2)` 分割；frontmatter 区域逐行解析 `key: value`，去除空白和引号；返回 `(meta, parts[2].strip())`。非 frontmatter 文本返回 `({}, text)`。
