import json
from config import DEFAULT_MAX_TOKENS, MODEL_ID
from prompt import get_system_prompt
from llm import call_llm
from utils import assistant_message_dict


def agent_loop(messages: list):
    # 将最大的token数量设置为默认的值8000，未来这个值可能会变
    max_tokens = DEFAULT_MAX_TOKENS
    # 把模型先设置模型 未来如果这个默认模型不能用，可能会切换备用模型
    model = MODEL_ID
    while True:
        # 获取系统提示词
        system = get_system_prompt()
        # 调用大模型获取回复
        response = call_llm(system, messages, max_tokens, model)
        # 获取助手返回的消息
        choice = response.choices[0]
        assistant = choice.message
        # 消耗的token在choice.usage
        # 将助手的回复以字典的形式添加到消息列表
        messages.append(assistant_message_dict(assistant))
        # 如果助手没有工具调用，则终止循环
        if not assistant.tool_calls:
            return
