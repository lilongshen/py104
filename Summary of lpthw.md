## Summary

- 回顾练习过程：整体是否顺畅？哪些练习比较顺畅？哪些练习遇到了困难？
- 复盘解题过程：遇到困难，你是如何解决的？请举一例，详细描述你发现问题、探索问题、解决问题的全过程和各环节时长。你做了哪些尝试？哪些环节可以做得更好？
- 什么情况下，你更容易进入心流状态及心流持续更长时间？什么情况下，你很难进入心流状态？
- 为了更容易进入心流状态、享受更长的心流时长，你打算提前做哪些准备？

### 背景

- 2016两次开始到放弃，没有动力，没有兴趣，没有坚持。
- 2017开始从各方面改变，听从内心决定依然要学习编程。

### 回顾

- 模仿练习整体还算顺利，出错点如下：
  - 拼写单词错误。
  - 连接符是 `_`  ,不是 ` -`
  - 半角符号，不是全角符号
  - 区分args, argv。`argv`是一个关键词，“参数变量(argument variable)”，是一个非常标准的编程术语。args非关键词，仅可表示变量名，多个参数的意思。
  - 区分`=`，`==`，`===`，`=`是表示赋值，例如键盘输入赋值，数字字符串赋值等。`==`表示相等，例如应用于boolean运算。`===`表示严格相等，两者完全一样。
  - 遗漏冒号 `:`

### 复盘

- 解题过程中遇到新的函数，就需要查python官方文档，看解释，模仿范例。例如练习20中，`seek`函数，`open`函数，`read`函数，`readline`函数，第一次遇到都没有头绪，有些从英文字面理解，能猜出意思，但是具体用法和规范必须查找文档。查找文档后可以继续去stackoverflow查其他人的问题，再去博客看其他人的总结。
- 举例：练习20中的`cuurent_line`两次加1，可以用`+=`符号来简化代码。


```python
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
```

- 还可以做到更好，在学习循环之后，回头把练习20中的`cuurent_line`的累加用for循环表示，精简了代码。


```python
# print three lines:
print "Let's print three lines:"

for current_line in range(1,4):
	print_a_line(current_line, current_file)
```

### 心流

- **进入心流的状态**

1. 首先是吃饱睡足之后，才有进入心流的可能。
2. 实现确定目标，明确今天要完成哪些事项。
3. 过程中奖励自己，享受成就感。代码实现正确后，对自己说肯定的话语。例如：XXX，你牛X。

- **难以进入心流的状态**

1. 饥饿、疲惫的状态。
2. 目标不明确。
3. 对任务的难度和深度估计不足，盲目乐观，导致计划安排过满，总是担心时间不够用，完不成task list。

- 为了更容易进入心流状态、享受更长的心流时长，我打算储备体能，设定目标，全情投入。不对任务完成数量而焦虑，更加注重任务完成的质量。期间不断肯定自己，做到powerful and confidence。


















​