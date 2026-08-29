import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载.env文件中值到环境变量中，override=True表示如果环境变量里已经有同名变量了，则进行覆盖
load_dotenv(override=True)
# 从环境变量中获取模型名称
MODEL_ID = os.environ["MODEL_ID"]
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"], base_url=os.environ["OPENAI_BASE_URL"]
)
# 默认的是大token数量
# 指的是模型输出的token的上限(也就是生成的内容) 一般来说一个汉字等于1~2个token
DEFAULT_MAX_TOKENS = 8000
