---
name: agent-directory-config
description: 项目目录与限制常量：skills、.task_outputs/tool_results、.transcripts、.memory 等
type: project
---

- `WORKDIR = Path.cwd()`
- `SKILLS_DIR = WORKDIR / "skills"`
- `TOOL_RESULTS_DIR = WORKDIR / ".task_outputs" / "tool_results"`
- `TRANSCRIPTS_DIR = WORKDIR / ".transcripts"`
- `MEMORY_DIR = WORKDIR / ".memory"`，启动时确保存在
- `MEMORY_INDEX = MEMORY_DIR / "MEMORY.md"`
- `MAX_BYTES = 10000`
- `PERSIST_THRESHOLD = 1000`
- `KEEP_RECENT = 3`
- `CONTEXT_LIMIT = 100000`
- `MAX_MESSAGES_LENGTH = 50`
- `CONSOLIDATE_THRESHOLD = 10`
