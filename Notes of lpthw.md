## Notes

1. `print` 代表输出，`#` 符号代表注释。

2. ```
   + plus 加号 
   - minus 减号
   / slash 斜杠 除法
   * asterisk 星号 乘法
   % percent 百分号 模除
   < less-than 小于号
   > greater-than 大于号
   <= less-than-equal 小于等于号
   >= greater-than-equal 大于等于号
   ```

3. 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

4. `=`的名字是等于(equal)，它的作用是为东西取名。`_`是下划线字符(underscore)，连接变量名。

5. ```
   Traceback (most recent call last):
     File "ex4.py", line 8, in <module>
       average_passengers_per_car = car_pool_capacity / passenger
   NameError: name 'car_pool_capacity' is not defined
   ```

   错误信息解析：

   第一行表示：系统开始追踪(最近一次调用的程序)
   第二行表示：搜寻到文件"ex4.py"，第8行出错。
   第三行显示：代码第8行内容
   第四行表示：出错原因是'car_pool_capacity'这个名字没有被定义过。
   所以要查询是否缺失定义，或拼写错误。

6. 格式化字符串`%s`, `%r`, `%d`.   `%s.” %”xxx

   `%s`, `%r`的区别：用`%r`显示的是变量“原始”的数据值，`%r`在打印的时候能够重现它代表的对象，但其他的符号用来给用户显示变量值。

   字符串`+`字符串，还是字符串。

7. ```
   print end1 + end2 + end3 + end4 + end5 + end6,
   print end7 + end8 + end9 + end10 + end11 + end12
   ```

   两个print之间有`,`，显示一行；两个print之间没有`,`，显示两行。

8. `"""`而不是`" " "`, 意思是说每两个双引号之间不能有空格。

9. 使用反斜杠 `\`(back-slash) 可以将难打印出来的字符放到字符串。针对不同的符号有很多这样的所谓“转义序列(escape sequences)。

10. `raw_input()` 获取终端输入，默认字符串。`x = int(raw_input())`，直接转换成数值。

11. `pydoc` 查看帮助文档。

12. `y = raw_input("Name? ")` 这句话会用 “Name?” 提示用户，然后将用户输入的结果赋值给变量 y。这就是我们提问用户并且得到答案的方式。

13. 命令行运行 `python ex13.py`,  `python`后面的都是参数(argument)。

    `import`语句，表示加入python的模块(modules)，或称作“库(libraries)。

    `argv`，表示参数变量(argument variable)，包含了传递给 Python 的参数。

    `script, first, second, third = argv` 将 `argv`进行“解包(unpack)，把 argv 中的东西解包，将所有的参数依次赋予左边的变量名。

14. `txt = open(filename)`  返回的是文件对象，不是文件内容。

15. 打开文件会用到open函数，标准的python打开文件语法如下：`open(name[,mode[,buffering]])`
    open函数的文件名是必须的，而模式和缓冲参数都是可选的。比如说有个a.txt的文本文件，存放在c:\text下，那么你要打开它可以这样操作：`x = open(r 'c:\text\a.txt')`  r可省略。用读的模式打开这个路径下的对应文本文件，如果要打开对像不存在，程序会报错。

    刚才打开文件过程中用到了‘r’这个参数，在文件打开过程中还会用到很多操作方法，都有不同的参数来表示。'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式。

16. ```
    close -- 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
    read -- 读取文件内容。你可以把结果赋给一个变量。
    readline -- 读取文本文件中的一行。
    truncate -- 清空文件，请谨慎使用该命令。
    write('stuff') -- 将stuff写入文件。
    ```

    `target = open(filename, 'w')`  open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。

17. 函数`len() `获得参数的长度，返回值是一个数字。

18. **command line summary**

    ls 查看文件夹中所有文件

    pwd 查看当前工作目录

    cd 进入下一级文件夹

    cd .. 进入上一级文件夹

    cd ~ 进入主目录

    mkdir 创建一个文件夹

    touch 创建一个文件

    ls -a 查看文件夹中所有的文件包括隐藏文件。 “.”开头的

    ls -l 以文件长度排序显示文件列表

    ls -t 以文件最后修改实践显示文件列表

    ls -alt 上述三者同时满足条件显示文件列表

    cp 复制文件   cp  a文件  b文件夹

    mv 移动文件 mv a文件  b文件夹   更改文件名 mv a文件  b文件

    rm  删除文件 永久删除，无法撤回

    rm -r  删除文件夹和文件夹内的文件，永久删除，无法撤回

    echo 接收字符串作为标准输出，并且显示到控制台。

    standard input, abbreviated as stdin, is information inputted into the terminal through the keyboard or input device.标准输入，简写为stdin，指信息通过键盘或其他输入设备输入到控制台。

    standard output, abbreviated as stdout, is the information outputted after a process is run.标准输出，简写为stdout，指信息由进程运行后信息被输出。

    standard error, abbreviated as stderr, is an error message outputted by a failed process.标准错误，简写为stderr，指由于错误进程输出的错误信息。

    输入和输出都是针对控制台而言的。

    \>  指令到文件的重新定向标准输出，并重写内容。

    cat  在控制台显示文件中的内容。以下三种是cat命令重定向到文件。cat代表显示命令，所以控制台显示。

    cat a文件 > b文件，本来是在控制台显示a文件，但是由于有 > ，标准输出cat a文件重新定向到b文件，结果本应该在控制台显示的内容，现在要在b文件内显示。 另外>有替代功能，b文件被>重写了，内容被替换成了a文件内容。

    \>> 指令到文件的重新定向标准输出，并增加新内容到旧内容后。

    cat a文件  >> b文件，同上，但是与上不同的是，>> 有追加功能，b文件被>>追加内容，内容中追加了a文件的内容。

    < 重定向标准输入到指令

    cat < a文件，<右边的表示标准输入，输入结果到<左边。此时，a文件是标准输入，内容显示在控制台。

    ｜ 表示pipe管道，指令到指令的重定向标准输出。

    cat a文件 | wc，管道左边表示标准输出，管道右边表示标准输入。通过 ｜ 重定向到wc，wc表示内容的行数，单词数和字符数。

    多个 ｜ 可以作为链条使用。cat a文件 ｜ wc ｜ cat < b文件，标准输出cat a文件通过管道传给wc，wc本要显示在控制台，但是通过｜又传给cat，最后cat重定向给b文件。

    sort表示标准输入，并且为标准输出内容按照字母序列排序，并输出到控制台。

    cat a文件 | sort > b文件，｜左侧标准输出，通过管道传给sort排序，又重定向到b文件中。

    uniq 表示唯一性，过滤临近的重复行内容并显示到控制台，不一定完全去除重复。

    sort a文件 | uniq 先对a文件排序，然后通过管道传给uniq，过滤临近重复，可以完全去除重复。

    grep 表示 "global regular expression print". 全局正则表达式显示。用规定形式查找文件内容，并且返回结果。

    区分大小写。grep -i 表示不敏感正则搜索，不区分大小写。

    grep -R表示查找目录中的所有文件，并输出符合条件的文件名和文件内容。R代表recursive递归。

    grep -Rl表示查找目录中的所有文件，只输出符合条件的文件名。-R 代表recursive递归， l 代表匹配的文件。

    sed 表示流编辑器。它接收标准输入并在显示数据之前根据正则表达式修改。类似于查找并替换。

    sed 's/snow/rain/' forests.txt 为例，s表示substitution替换，在sed中经常使用作为替换功能。snow表示寻找和被替换的内容，rain替换者。此例仅仅替换每行中的第一个snow。

    sed 's/snow/rain/g' forests.txt，此例中，g代表global全局，表示所有的snow都要被替换成rain。

    nano 命令行编辑器。类似于桌面端编辑器TextEdit 或者Notepad。nano 文件名，打开了编辑器。在编辑器中可以随意输入内容。编辑器下方是操作按钮，^表示ctrl键，其余为字母。例如ctrl O 表示保存。 O 表示输出。 ctrl X表示退出，X表示退出。ctrl G表示打开帮助。clear表示清空控制台，光标移到最上方。

    ~/.bash_profile 是储存环境变量的文件。当会话开始时，此文件会在执行指令前加载文件内容。

    ～代表用户主目录。 .代表隐藏文件。

    source ~/.bash_profile 表示在当前会话中激活更改。

    alias 表示创建键盘快捷键。

    USER="Lynn” 表示设置环境变量USER为名字Lynn。

    export表示使变量在当前会话引起的子会话都可用，这个方式使变量在程序中是全局的。

    echo $USER表示返回变量值。$总是用在返回变量值中。

    PS1表示命令行提示的标记和格式。export PS1=">> “设置了命令行变量并且输出了变量。从$标记变成了 >>标记。

    HOME变量是环境变量，表示显示主目录。

    PATH变量是环境变量，存储了一系列目录，由冒号隔开。每个目录都有自己执行的脚本，但是PATH变量只显示目录。

    env命令代表环境，返回当前用户的环境变量。

    env | grep PATH 显示单独环境变量的值。env标准输出通过管道传到grep，grep寻找PATH值，并且输出到控制台。

19. `def` 命令表示定义，用来创建一个函数，函数以`def`开头；

    函数名最好能够体现出函数的功能，函数名称只能以字母、数字和下划线 `_`组成，其中数字不能开头；

    函数名后紧跟(，参数必须放在圆括号 () 中才能生效，参数可有可无，多个参数要以逗号隔开，不能使用重复的参数名；

    紧跟着参数的是括号和冒号 `):` ，用冒号`:`结束定义函数行，然后开始下一行缩进；

    冒号以下，使用4个空格缩进，属于函数的内容；

    函数结束的位置取消了缩进。

    使用use”或“调用call 函数，要使用函数的名称；

    函数名称后紧跟着 `(`，括号后参数可有可无，与原函数对应，多个参数以逗号隔开，函数以 `)` 结尾。

    `run`, `call`, `use ` 是相同功能，调用函数。

20. `file.seek(off, whence=0)`：从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。

21. ```
    and 与
    or 或
    not 非
    != (not equal) 不等于
    == (equal) 等于
    > = (greater-than-equal) 大于等于
    <= (less-than-equal) 小于等于
    True 真
    False 假
    ```

22. | NOT       | TRUE  |
    | --------- | :---: |
    | not False | True  |
    | not True  | False |

    | OR             | TRUE? |
    | -------------- | ----- |
    | True or False  | True  |
    | True or True   | True  |
    | False or True  | True  |
    | False or False | False |

    | AND             | TRUE? |
    | --------------- | ----- |
    | True and False  | False |
    | True and True   | True  |
    | False and True  | False |
    | False and False | False |

    | NOT OR               | TRUE? |
    | -------------------- | ----- |
    | not (True or False)  | False |
    | not (True or True)   | False |
    | not (False or True)  | False |
    | not (False or False) | True  |

    | NOT AND               | TRUE? |
    | --------------------- | ----- |
    | not (True and False)  | True  |
    | not (True and True)   | False |
    | not (False and True)  | True  |
    | not (False and False) | True  |

    | !=     | TRUE? |
    | ------ | ----- |
    | 1 != 0 | True  |
    | 1 != 1 | False |
    | 0 != 1 | True  |
    | 0 != 0 | False |

    | ==     | TRUE? |
    | ------ | ----- |
    | 1 == 0 | False |
    | 1 == 1 | True  |
    | 0 == 1 | False |
    | 0 == 0 | True  |

23. or 或

    not 非

    != (not equal) 不等于

    == (equal) 等于

    = (greater-than-equal) 大于等于

    <= (less-than-equal) 小于等于

    True 真

    False 假

24. 在“if语句”内部再放一个“if语句”，可以用来创建嵌套(nested)，其中的一个分支将引向另一个分支的子分支。

25. range（）函数.

    **函数原型**：`range`(*start*, *stop*[, *step*]):

    **参数含义**：start: 计数从start开始。默认是从0开始。例如: range(5)等价于range(0, 5)

    ​              	   stop: 计数到stop结束，**但不包括stop。**例如: range(0, 5) 是[0, 1, 2, 3, 4]没有5

    ​              	   step: 每次跳跃的间距，默认为1。例如: range(0, 5)等价于 range(0, 5, 1)

26. for循环会自动计次，从start 到stop自动+step计次。无需加值操作。如果不去掉加值操作，会发生理解困难，产生如下效果：

    ```
    for i in range(0, 5):
        print i
        i += 2
        print i
        print 'end'
    ```

    ```
    结果
    0
    2
    end
    1
    3
    end
    2
    4
    end
    3
    5
    end
    4
    6
    end
    ```

    ```
    而不是
    0
    2
    end
    2
    4
    end
    4
    6
    end
    ```

27. 列表（list），有序的项目列表，通过数值索引来访问

    ```
    hairs = ['brown', 'blond', 'red']
    eyes = ['brown', 'blue', 'green']
    weights = [1, 2, 3, 4]
    ```

28. | 1    | list.append(obj)在列表末尾添加新的对象              |
    | ---- | ---------------------------------------- |
    | 2    | list.count(obj)统计某个元素在列表中出现的次数           |
    | 3    | list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
    | 4    | list.index(obj)从列表中找出某个值第一个匹配项的索引位置      |
    | 5    | list.insert(index, obj)将对象插入列表           |
    | 6    | list.pop(obj=list[-1\])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
    | 7    | list.remove(obj)移除列表中某个值的第一个匹配项          |
    | 8    | list.reverse()反向列表中元素                    |
    | 9    | list.sort([func])对原列表进行排序                |

29. 序数(ordinal number)，从1开始，表示事物的顺序。基数(cardinal number)，从0开始，表示索引(index)。

30. 在许多操作系统中可以使用`exit(0)`来中止程序。

31. `split`将字符串转化为列表，`' 1  2  3 '.split()` returns `['1', '2', '3']`。

32. 字典(dictionary)是用来做映射或者存储你需要的键值对。通过key来访问value，即映射（"mapping"）。

33. 模块（module）.

    包含一些函数和变量的python文件

    你可以导入这个文件

    你可以用`.`操作符访问这个模块的函数和变量

34. class(类)：告诉python去创建一个新类型。object(对象)：有两种意思，事物的基本类型，或者事物的实例化。instance(实例)：你通过python创建一个类所获得的。def：用来在类中定义一个函数。self：在一个类包含的函数中，self是一个用来访问实例或对象的变量。inheritance：概念，表示一个类可以继承另一个类的特征,就像你和你的父母。composition：概念，表示一个类可以包含其他类,就像汽车轮子。 attribute：类所拥有的特性，通常是变量。is-a：惯用语，表示一个东西继承自另一个东西(a),像在“鲑鱼”是“鱼”。 has-a：惯用语，表示由其他事情或有一个特征(a),如“鲑鱼有嘴。”

35. 示例

```
class Actor(object):
	def book(self, cellar, dad)
# class Actor has-a function named book that takes self and cellar, dad parameters. 
```

```
cattle = Coach()
# Set cattle to an instance of class Coach.
```

```
bulb.beast(breakfast)
# From bulb get the beast function, and call it with parameters self, breakfast.
```

```
dress.cap = 'balloon'
# From dress get the cap attribute and set it to 'balloon'.
```

```
class Bite(Color):
# Make a class named Bite that is-a Color.
```

```
class Curve(object):
	def caption(self, bean)
# class Curve has-a function named caption that takes self and bean parameters.
```



## Python Mistakes

**Spelling**

- 连接符是 `_`  ,不是 ` -`
- 注意代码格式，不要太长，符号前后有空格。
- 全角符号害死人，全部用半角。
- 区分args, argv。`argv`是一个关键词，“参数变量(argument variable)”，是一个非常标准的编程术语。args非关键词，仅可表示变量名，多个参数的意思。
- 区分`=`，`==`，`===`，`=`是表示赋值，例如键盘输入赋值，数字字符串赋值等。`==`表示相等，例如应用于boolean运算。`===`表示严格相等，两者完全一样。




## GIT教程

- git是什么？

  Git是目前世界上最先进的分布式版本控制系统（没有之一）。

- 如何安装git？

  推荐方法：安装Homebrew

  `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”`

  配置Homebrew

  `echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile`

  安装git

  `brew install git`

- 初始化一个Git仓库，使用`git init`命令。

  添加文件到Git仓库，分两步：

  第一步，使用命令`git add <file>`，注意，可反复多次使用，添加多个文件；

  第二步，使用命令`git commit`，完成。

- 要随时掌握工作区的状态，使用`git status`命令。

  如果`git status`告诉你有文件被修改过，用`git diff`可以查看修改内容。

- HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`。

- 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。

- 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。

- 工作区（Working Directory）就是你在电脑里能看到的目录

- 版本库（Repository）工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。

- **Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。**

  **第一步是用`git add`把文件添加进去，实际上就是把文件修改添加到暂存区；**

  **第二步是用`git commit`提交更改，实际上就是把暂存区的所有内容提交到当前分支。**

  **因为我们创建Git版本库时，Git自动为我们创建了唯一一个master分支，所以，现在，`git commit`就是往master分支上提交更改。**

  **每次修改，如果不add到暂存区，那就不会加入到commit中。**

  场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout — file`。

  场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD file`，就回到了场景1，第二步按场景1操作。

  场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

- 命令`git rm`用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

- **Github提供Git仓库托管服务，只要注册一个GitHub账号，就可以免费获得Git远程仓库。本地Git仓库和GitHub仓库之间的传输是通过SSH加密的。**

- **要关联一个远程库，使用命令`git remote add origin git@server-name:path/repo-name.git`；**

- **关联后，使用命令`git push -u origin master`第一次推送master分支的所有内容；**

  **此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改；**

- **`git pull origin master` 相当于`git fetch` 和 `git merge`。`git fetch` 表示从远程的origin的master主分支下载最新的版本到本地的master分支上，然后可以进行比较`git diff`，最后进行合并`git merge`。**

- 分布式版本系统的最大好处之一是在本地工作完全不需要考虑远程库的存在，也就是有没有联网都可以正常工作，当有网络的时候，再把本地提交推送一下就完成了同步。

- 要克隆一个仓库，首先必须知道仓库的地址，然后使用`git clone`命令克隆。

- Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。

- Git鼓励大量使用分支：

  查看分支：`git branch`

  创建分支：`git branch <name>`

  切换分支：`git checkout <name>`

  创建+切换分支：`git checkout -b <name>`

  **合并某分支到当前分支：`git merge <name>`**

  删除分支：`git branch -d <name>`

  当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

  用`git log —graph`命令可以看到分支合并图。

  Git分支十分强大，在团队开发中应该充分应用。

  合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

  修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；

  当手头工作没有完成时，先把工作现场`git stash`一下，然后去修复bug，修复后，再`git stash pop`，回到工作现场。

  开发一个新feature，最好新建一个分支；

  如果要丢弃一个没有被合并过的分支，可以通过`git branch -D <name>`强行删除。

- 查看远程库信息，使用`git remote -v`；

  本地新建的分支如果不推送到远程，对其他人就是不可见的；

  从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用git pull抓取远程的新提交；

  在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；

  建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；

  从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。

- 命令`git tag <name>`用于新建一个标签，默认为HEAD，也可以指定一个commit id；

  `git tag -a <tagname> -m "blablabla..`."可以指定标签信息；

  `git tag -s <tagname> -m "blablabla...`"可以用PGP签名标签；

  命令`git tag`可以查看所有标签。

  命令`git push origin <tagname>`可以推送一个本地标签；

  命令`git push origin —tags`可以推送全部未推送过的本地标签；

  命令`git tag -d <tagname>`可以删除一个本地标签；

  命令`git push origin :refs/tags/<tagname>`可以删除一个远程标签。

- 在GitHub上，可以任意Fork开源仓库；

  自己拥有Fork后的仓库的读写权限；

  可以推送pull request给官方仓库来贡献代码。


Git 官网[http://git-scm.com]([http://git-scm.com](http://git-scm.com))

全文总结来自廖雪峰[Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

