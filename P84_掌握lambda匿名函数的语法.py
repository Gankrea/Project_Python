"""
函数的定义中

· def关键字,可以定义带有名称的函数

· lambda关键字,可以定义匿名函数(无名称)

有名称的函数,可以基于名称重复使用。

无名称的匿名函数,只可临时使用一次。

匿名函数定义语法:
lambda 传入参数:函数体(一行代码)
· lambda 是关键字,表示定义匿名函数

· 传入参数表示匿名函数的形式参数,如:x,y表示接收2个形式参数
· 函数体,就是函数的执行逻辑,要注意:只能写一行,无法写多行代码

"""
# 使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用

def test_func1(compute1):
    result = compute1(1, 2)
    print(result)


def compute1(x, y):
    return x + y


test_func1(compute1)


# 也可以通过lambda关键字,传入一个一次性使用的lambda匿名函数
def test_func(compute):
    result = compute(1, 2)
    print(result)

# 计算流程
test_func(lambda x, y: x + y)
