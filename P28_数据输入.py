"""
获取键盘输入的数据 input("提示信息")
例如 age = input()
注意！
    无论键盘输入什么数据类型，获取到的都是字符串类型
    number = input("请输入你的年龄")
    print("数据类型是：",type(number))
    输出 数据类型是： <class 'str'>
"""
name = input("你的名字是")
print("你的名字是：%s" % name)
# 我们可以用数据类型的转换
"""
数据类型转换
int()
float()
string()
"""
number2 = input("请输入你的年龄")
print("你的年龄是 %d" % int(number2),type(int(number2)))

# 小练习
name=input("请输入你的名字")
type = input("IVP用户")
print(f"你好：{name},你是尊贵的{type}用户，欢迎光临")
