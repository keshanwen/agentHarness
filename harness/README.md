

如果你不加这句话，让它用CMD，它会先使用linux bash命令先尝试，失败了以后才会换到CMD命令


# 输出为什么要加限制，不可以无限输出吗？
因为技术和成本双重原因，不可能无限输出，必须限制
1. 算力成本 每个token都需要计算，无限输出=无限的GPU的无限消耗，成本失控
2. 工程的稳定性 模型可能会陷入死循环，或者胡说八道
3. 另在技术成本 LLm内部用是transformer架构，生成的自回归的 一个字一个字往外蹦，长度越长计算量呈平方级增加，越来效果越差

# harness engineering 驾驭工程
指的是AI智能体设计和构建约束机制、反馈回路，工作流程控制，以及持续改进循环的系统工程实践

# del /q tmp\\*
del  windows的删除文件的命令 等同于linux rm 
/q 静默模式 quiet  不提示确认，直接删除
tmp/* 删除tmp目录下面的所有的文件

请帮我读取a.txt、b.txt、c.txt三个文件的内容并输出结果
a和c成功了，b失败了
然后你把这个结果 反馈给AI大模型

#claude code中的/bwt指令是不是也是类似的原理，开启一个子进程，用主Agent的上下文发起临时查询？\

正确，核心机制也是类似于临时子任务的思路，但是细节不太一样

/btw 指令  不是开启独立子进程，而在当前会话中创建一个轻量级的临时链，复用主会话的上下文和提示词缓存，但是
回答后的结果不会写入主对话历史，实现零污染并行回答

# encoding 指定字符编码 通常为utf-8
# errors="replace" 指定解码失败的时候的处理策略，replace替换，指的是用 乱码符号�替换无法解码的字节，防止程序崩溃
# errors 有几个可选策略
  - strict 严格格式 如果遇到解码失败就会抛出UnicodeDecodeError错误
  - replace 容忍乱码，确保程序不中断，用�替换掉坏的字节
  - ignore 跳过坏字节，丢弃异常数据
  - backslashreplace 用\xXX转义  如果遇到解码失败显示成原始字节



skill中 scripts/目录用于存放可执行脚本，可以帮助skill实现功能的复杂核心执行
- my-skill
  - SKILL.md 指令文件 加载到上下文中去
  - scripts
    - extract.py 提取pdf文档的内容
    - process.h  shell脚本
    - data
      - config.json 辅助数据

- 执行方式 calude 通过bash工具调用脚本，不加载源码到上下文中
- 触发时机  skill.md文件加载后，claude会根据指令 决定什么时候执行哪个脚本，获取什么结果
- 输入输出 通过命令行参数传递输入参数，通过stdout/stderr返回结果

常用脚本类型
python 可以处理复杂逻辑 pDF解析 文件格式转式
shell/bash 系统操作相关的命令 配置环境变量
node.js  前端相关脚本 可以实现打包构建 npm run build 解析AST语法


_  - 中划线和下划线并没有固定硬性要求
目录名 用中划线  tool-results 这是个linux惯例
变量名 下划线  tool_result
域名   my-site
字段名  tool_result
CSS类名  my-home

messages = [
 user,
 assistant, tool_call.id
 tool,
 user,
 assistant(两个tool call ids) 开始要求新的一轮工具调用，要求之前的tool call都要已经有了对应的tool
 tool,
 tool
]

messags = [
  {"role":"user"},
  {"role":"assistant","tool_calls":[{"id":"call_ids"},{}]}
]

# 整个messages都是提示词
messages = [
  #不变放前面
  {"role":"system","content":"你是一个Agent"},
  {"role":"user"}
  ...
  # 有可能变化的放在后面

]

#  rounds_since_todo
1. 不管有没有使用todowrite,不管现在有没有当前尚未完成的任务，都会每3轮一次。
2. 现在这个提醒放在了messages里面，会污染上下文


执行任务，计算1+1=？和2+2=？和3+3=？和4+4=？和5+5=？（先列出5个步骤再执行）

有些Agent会给记忆添加一个半衰期的概念
每个记忆文件有记录的时间

指的是记忆的重要性/权重会随着时间而指数衰减，越久远的记忆影响越小
新的权重 =原始权重x(0.5)^(时间差/半衰期)

# 比如codex, 记忆和自定义指令冲突时，以哪个为准
在codex里，当记忆memories和自定义指令 AGENTS.md冲突的时候，以正定义指令为准

AutoDream
