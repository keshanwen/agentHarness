from pathlib import Path
from config import WORKDIR
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

# 此函数接收一个路径，返回一个Path
def safe_path(p: str) -> Path:
    # 通过WORKDIR与p拼接，并调用resolve方法，得到p的绝对路径
    path = (WORKDIR / p).resolve()
    # 判断path是不是在WORKDIR工作区内的子路径，如果不是则抛异常
    if not path.is_relative_to(WORKDIR):
        raise ValueError(f"超出工作区:{p}")
    # 返回最终安全生成的路径对象
    return path

def extract_text(content) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    return str(content)