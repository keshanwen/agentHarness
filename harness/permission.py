from config import WORKDIR

# 定义禁止执行的命令列表
DENY_LIST = [
    # rm -rf / 强制递归删除根目录 删除系统
    # sudo 以root权限执行
    # shutdown/reboot 关机/重启
    # mkfs 格式化磁盘
    # dd if= 用零覆盖磁盘 销毁所有的数据 不可恢复
    # > /dev/sda 重定向到块设备，会破坏分区表 会导致磁盘损坏
    "rm -rf /",
    "sudo",
    "shutdown",
    "reboot",
    "mkfs",
    "dd if=",
    "> /dev/sda",
]
# 定义需要用户确认或者审批的破坏性命令
DESTRUCTIVE = ["rm ", "> /etc/", "chmod 777", "del ", "erase "]


def check_permission(tool_name: str, args: dict) -> str | None:
    if tool_name == "bash":
        for pattern in DENY_LIST:
            if pattern in args.get("command", ""):
                print(f"\n\x1b[31m⛔ 已拦截：'{pattern}'\x1b[0m")
                return "禁止列表拒绝权限"
        for kw in DESTRUCTIVE:
            if kw in args.get("command", ""):
                print(f"\n\x1b[33m⚠  可能破坏性的命令\x1b[0m")
                print(f"工具:{tool_name}({args})")
                # 提示用户允许 执行输入y或yes才继续执行
                choice = input("是否允许执行?[y/N]").strip().lower()
                # 如果用户输入的不是y和yes
                if choice not in ("y", "yes"):
                    return "用户拒绝执行"
    if tool_name in ("write_file", "edit_file"):
        # 获取要写入或编辑文件的路径
        path = args.get("path", "")
        # 如果检查到要写入的文件不在当前目录下
        if not (WORKDIR / path).resolve().is_relative_to(WORKDIR):
            print(f"\n\x1b[33m⚠  在工作区外面写入\x1b[0m")
            print(f"工具:{tool_name}({args})")
            # 提示用户允许 执行输入y或yes才继续执行
            choice = input("是否允许执行?[y/N]").strip().lower()
            # 如果用户输入的不是y和yes
            if choice not in ("y", "yes"):
                return "用户拒绝执行"
    return None
