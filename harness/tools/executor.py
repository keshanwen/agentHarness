import inspect
from tools.handlers import TOOL_HANDLERS


# 接收工具名称和参数字典，返回结果args={"name":"zhangsan","age":18,"command":'dir'}
def execute_tool(name: str, args: dict) -> str:
    # 根据工具名称从TOOL_HANDLERS获取对应的处理函数
    handler = TOOL_HANDLERS.get(name)
    # 如果没有找到处理函数，则返回错误提示
    if not handler:
        return f"未知工具: {name}"
    # 获取处理函数的参数签名
    sig = inspect.signature(handler)
    # 从输入参数中筛选出处理函数所需要的有效参数
    valid = {k: v for k, v in args.items() if k in sig.parameters}
    return handler(**valid)
