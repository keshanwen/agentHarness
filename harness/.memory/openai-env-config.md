---
name: openai-env-config
description: 项目通过 .env 配置 OpenAI 兼容客户端，使用 MODEL_ID、OPENAI_API_KEY、OPENAI_BASE_URL
type: project
---

`config.py` 使用 `load_dotenv(override=True)` 加载 `.env`，覆盖已有同名环境变量。

- 从 `os.environ["MODEL_ID"]` 读取模型名称。
- 使用 `OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url=os.environ["OPENAI_BASE_URL"])` 初始化客户端。
- 默认输出 token 上限 `DEFAULT_MAX_TOKENS = 8000`；注释说明一个汉字约 1~2 个 token。
