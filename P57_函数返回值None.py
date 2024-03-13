"""
函数没写return，还是会返回 None

在if判断上
None等同于False

声明无初始值的变量
定义变量，但暂时不需要变量有具体的值，可以用None来代替
name=None

"""

def say_hi():
    print('hello')
    return None

result = say_hi()
print(f"无返回值函数，返回的内容是{result}")

# NoneType 表示 空的，无意义的
print(f"无返回值函数，返回的类型是{type(result)}")
