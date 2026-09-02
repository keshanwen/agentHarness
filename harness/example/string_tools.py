import re
import unicodedata


def slugify(text: str) -> str:
    """
    将任意文本转换为 URL 友好的 slug。
    规则：小写、非字母数字字符转为连字符、去除首尾连字符。
    """
    # 规范化 Unicode（将重音字符分解为基础字符）
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    # 转为小写
    text = text.lower()
    # 非字母数字字符转为连字符
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # 去除首尾连字符
    text = text.strip('-')
    return text
