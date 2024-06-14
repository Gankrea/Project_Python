# 函数可以作为参数传入另一个函数内
def test_func(compute):
    result = compute(1, 2)
    print(result)


# 定义一个函数,准备作为参数传入另一个函数
def compute(x, y):
    return x + y


# 调用,并传入函数
test_func(compute)

"""
1.函数本身是可以作为参数,传入另一个函数中进行使用的。

2.将函数传入的作用在于:传入计算逻辑,而非传入数据。
"""