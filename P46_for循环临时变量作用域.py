"""
for 临时变量 待处理数据集
    循环满足条件时执行的代码

临时变量的作用域：
在编程规范上，作用范围(作用域)，只限定在for循环内部

如果在for循环外部访问临时变量
实际上是可以访问到
在编程规范上是不被允许，不建议这么做的

代码示例：
# 不符合代码规范的代码
for i in range(5):
    print(i)
# 这里的i打印的是for循环内部的临时变量
该操作是不被允许，不建议的
print(i)

# 正确示例
i = 0
for i in range(5):
    print(i)
# 打印的是最上面的 i = 0
print(i)
"""