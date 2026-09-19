---
name: project-uses-uv-pytest
description: 项目使用 uv 管理依赖，使用 pytest 测试，包含多个 Python 模块和 skills
type: project
---

根目录包含 `pyproject.toml` 和 `uv.lock`，表明使用 uv 管理 Python 依赖。存在 `.pytest_cache`，表明使用 pytest。根目录模块包括 `agent.py`、`config.py`、`history.py`、`hooks.py`、`llm.py`、`main.py`、`memory.py`、`prompt.py`、`skills.py`、`tools/`、`utils.py`。`skills/` 下可见 `code-review` 和 `commit`。
