"""
注意：
函数体在遇到return之后就结束了，所以写在return后的代码不会执行
"""
# 定义一个求和函数，x,y是形参
def add(x,y):
    # 把x和y的和赋值给number
    number = x+y
    # 把number的值返回给add()函数
    return number
# 用r变量接收结果(传入实参)

# 变量 = 函数(参数)
r = add(100,21)
# 打印结果
print(r)