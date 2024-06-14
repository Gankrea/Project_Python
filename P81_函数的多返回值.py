"""
当一个函数要有多个返回值时

def test_return():
    return 1, 2

x, y = test_return()
print(x)    # 1
print(y)    # 2
按照返回值的顺序,写对应顺序的多个变量接收即可
变量之间用逗号隔开
支持不同类型的数据return
"""
def sound():
    return 10, "hello"

x,y=sound()
print(x)
print(y)
