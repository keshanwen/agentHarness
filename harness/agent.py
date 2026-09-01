import json
from config import DEFAULT_MAX_TOKENS, MODEL_ID
from prompt import get_system_prompt
from llm import call_llm
from utils import assistant_message_dict
from tools.executor import execute_tool
from hooks import trigger_hooks


# 定义变量,用于记录上次todo_write调用以来的轮数
rounds_since_todo = 0

def agent_loop(messages: list):
    # 声明这是全局变量
    global rounds_since_todo
    # 将最大的token数量设置为默认的值8000，未来这个值可能会变
    max_tokens = DEFAULT_MAX_TOKENS
    # 把模型先设置模型 未来如果这个默认模型不能用，可能会切换备用模型
    model = MODEL_ID
    while True:
        # 获取系统提示词
        system = get_system_prompt()
        if rounds_since_todo >= 3 and messages:
            messages.append(
                {
                    "role": "user",
                    "content": "<reminder>请及时更新你的todo列表</reminder>",
                }
            )
            print(f"\x1b[33m请更新你的todo列表\x1b[0m")
            rounds_since_todo = 0
        # 调用大模型获取回复
        response = call_llm(system, messages, max_tokens, model)
        # 获取助手返回的消息
        choice = response.choices[0]
        assistant = choice.message
        # 消耗的token在choice.usage
        # 将助手的回复以字典的形式添加到消息列表
        messages.append(assistant_message_dict(assistant))
        # 每一轮调用让计数器加1
        rounds_since_todo += 1
        # 如果助手没有工具调用，则终止循环
        if not assistant.tool_calls:
            # 调用trigger_hooks函数，触发名为Stop的钩子，传入当前的消息列表
            force = trigger_hooks("Stop", messages)
            # 如果force有值说明活没干完，也就是hook返回了需要进一步处理的信息
            if force:
                # 如果有值，则将其作为用户角色的消息添加到消息列表中
                messages.append({"role": "user", "content": force})
                # 继续while循环，重新进入 agent loop的流程
                continue
            return
        # 如果助手要调用某些人，则循环所有的工具调用
        for tool_call in assistant.tool_calls:
            # 获取工具名称
            name = tool_call.function.name
            # 获取解析工具参数
            args = json.loads(tool_call.function.arguments or "{}")
            # 触发PreToolUse这个钩子，判断是否允许工具执行
            blocked = trigger_hooks("PreToolUse", name, args)
            # 只要有一个钩子函数返回一个非None的值，后面的钩子就不走了，
            if blocked:
                # 将阻止信息以tool角色的形式添加到消息列表中
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(blocked),
                    }
                )
                continue

            output = execute_tool(name, args)
            # 触发PostToolUse钩子，并进行后置处理
            trigger_hooks("PostToolUse", name, args, output)
            # 如果本次调用的工具就是todo_write,则也重置轮数计数器为0
            if name == "todo_write":
                rounds_since_todo = 0
            # 把工具调用的结果以特定的工具格式添加到消息列表
            messages.append(
                {"role": "tool", "tool_call_id": tool_call.id, "content": output}
            )
