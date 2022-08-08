# 函数

# 函数是带名字的代码块，用于
# 完成具体的工作。要执行函数定义的特定任务，可调用 该函数。需要在程序中
# 多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该
# 任务的函数，让Python运行其中的代码即可。你将发现，通过使用函数，程序
# 编写、阅读、测试和修复起来都更加容易。

# 定义函数
# 下面是一个打印问候语的简单函数，名为greet_user() ：
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")

greet_user()


# 使用关键字def 来告诉Python，你要
# 定义一个函数。这是函数定义 ，向Python指出了函数名，还可能在圆括号内指出函
# 数为完成任务需要什么样的信息。在这里，函数名为greet_user()，它不需要任
# 何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）。最后，定
# 义以冒号结尾。

# 紧跟在def greet_user(): 后面的所有缩进行构成了函数体。
# """"""中的文本是称为文档字符串 （docstring）的注释，描述了函数是做什么的。文档字符串用三引号
# 括起，Python使用它们来生成有关程序中函数的文档。

# 代码行print("Hello!") 是函数体内的唯一一行代码，因此
# greet_user() 只做一项工作：打印Hello! 。

# 要使用这个函数，可调用它。函数调用 让Python执行函数的代码。要调用 函数，
# 可依次指定函数名以及用圆括号括起的必要信息
# 由于这个函数不需要
# 任何信息，调用它时只需输入greet_user() 即可。



# 向函数传递信息
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello,{username.title()}!")

greet_user("jease")
# 在函数定义def greet_user() 的括号内添加username  即添加参数

# 实参和形参
# 在函数greet_user() 的定义中，变量username 是一个形参 （parameter），
# 即函数完成工作所需的信息。在代码greet_user('jesse') 中，值'jesse' 是
# 一个实参 （argument），即调用函数时传递给函数的信息。调用函数时，将要让函
# 数使用的信息放在圆括号内。在greet_user('jesse') 中，将实参'jesse' 传
# 递给了函数greet_user() ，这个值被赋给了形参username 。

# 注意 　大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变
# 量称为实参或将函数调用中的变量称为形参，不要大惊小怪。