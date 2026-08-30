import json
from config import DEFAULT_MAX_TOKENS, MODEL_ID
from prompt import get_system_prompt
from llm import call_llm
from utils import assistant_message_dict
from tools.executor import execute_tool
from permission import check_permission
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
        # 如果助手要调用某些人，则循环所有的工具调用
        for tool_call in assistant.tool_calls:
            # 获取工具名称
            name = tool_call.function.name
            # 获取解析工具参数
            args = json.loads(tool_call.function.arguments or "{}")
            print(f"\x1b[36m {name} {json.dumps(args,ensure_ascii=False)} \x1b[0m")
            # 对工具调用进行权限检查
            reason = check_permission(name, args)
            # 如果没有通过权限检查，将权限被 拒接的原因信息添加到消息列表里
            if reason is not None:
                messages.append(
                    {
                        "role": "tool",  # 角色为工具
                        "tool_call_id": tool_call.id,  # 关联的工具ID
                        "content": reason,  # 拒绝的原因
                    }
                )
                # 如果本次工具调用失败了，则继续调用下一个
                continue
            # 执行工具，获取输出的结果
            output = execute_tool(name, args)
            # 把工具调用的结果以特定的工具格式添加到消息列表
            messages.append(
                {"role": "tool", "tool_call_id": tool_call.id, "content": output}
            )