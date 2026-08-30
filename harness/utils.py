# 工具函数，可以把pydantic类型的大模型回复消息对象转成字典
def assistant_message_dict(message) -> dict:
    # 使用model_dump可以把对象转字典，排除值为None的项
    data = message.model_dump(exclude_none=True)
    # 把角色的类型设置为助手
    data["role"] = "assistant"
    return data

# 参数为data(字节类型或None)返回一个字符串
def decode_subprocess_output(data: bytes | None) -> str:
    if not data:
        return ""
    for encoding in ("utf-8", "gbk", "cp936"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")
