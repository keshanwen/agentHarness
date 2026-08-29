# 定义一个提示词片段的字典
PROMPT_SECTIONS = {
    # 是一个多行字符串，作为智能体的系统身份提示
    "identity": (
        f"你是一个编程Agent,直接行动，不要解释"
        f"你将在macOS环境下执行任务，使用zsh命令完成任务"
    )
}


def get_system_prompt() -> str:
    return PROMPT_SECTIONS["identity"]
