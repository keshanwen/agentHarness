import os
import subprocess
from utils import decode_subprocess_output


def run_bash(command: str) -> str:
    # 定义一些危险的命令列表
    dangerous = ["rm -rf", "sudo", "shutdown", "reboot", "> /dev/"]
    # 如果要执行的命令中包含任何一个危险命令，
    if any(d in command for d in dangerous):
        # 则返回错误提示，拦截拒绝执行危险命令
        return "错误:危险命令已经被拦截"
    try:
        # 得到的stdout和stderr是二进制的字节序列
        result = subprocess.run(
            command,  # 要执行的命令
            shell=True,  # 在shell中执行
            cwd=os.getcwd(),  # 把当前的工作目录设置为当前的路径
            capture_output=True,  # 捕获标准输出和标准错误输出
            timeout=120,  # 超时时间设置为120秒
        )
        out = decode_subprocess_output(
            (result.stdout or b"") + (result.stderr or b"")
        ).strip()
        return out[:500000] if out else "(无输出)"
    except subprocess.TimeoutExpired:
        return "错误： 超时(120秒)"
    except (FileNotFoundError, OSError) as e:
        return f"错误:{str(e)}"


# 定义字典，把工具的名称和真正的处理函数关联起来
TOOL_HANDLERS = {"bash": run_bash}
