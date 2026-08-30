# 用于定义工具的函数，接收函数名称、函数描述、属性和必填的字段,返回一个字典
def _fn_tool(
    name: str, description: str, properties: dict, requried: list[str]
) -> dict:
    return {
        "type": "function",  # 类型是函数
        "function": {  # 函数的具体内容
            "name": name,  # 函数名称
            "description": description,  # 函数描述
            "parameters": {  # 参数设置，是一个对象，包含属性和必需字段
                "type": "object",
                "properties": properties,
                "requried": requried,
            },
        },
    }


TOOLS = [
    _fn_tool("bash", "执行一条shell命令", {"command": {"type": "string"}}, ["command"])
]
