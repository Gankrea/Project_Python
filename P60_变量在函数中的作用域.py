"""
局部变量：
    定义在函数体内部的变量，只有在函数体内部生效
作用：在函数体内部，临时保存数据，当调用完后，就销毁局部变量

全局变量：
    在函数体外，外部都能生效的变量

global关键字：
    声明该变量变成全局变量
"""

# 局部变量
def test_1():
    num = 100
    print(num)

test_1()    # 100
# print(num)    报错：因为变量num在函数体test_1内部

"""---------"""

# 全局变量
trean = 300
def test_2():
    print(trean)

def test_3():
    print(trean)

test_2()    #100
test_3()    #100

"""---------"""

# global 关键字
trean = 10086

def test_10():
    print(trean)

def test_11():
    # global 关键字声明 把局部变量变成全局变量
    global trean
    trean = 10010
    print(trean)

test_10()   #10086
test_11()   #10010