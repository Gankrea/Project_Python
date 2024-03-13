"""
通过多行注释的形式，在函数体内进行说明解释
内容应写在函数体之前
"""
def add_sun(x, y):
    """
    这是两数相加求和的函数

    :param x: 形参x的说明
    :param y: 形参x的说明
    :return: 返回值的说明
    """
    # 函数体
    number = x + y
    return number  # 返回值

add_sun(10, 20)
