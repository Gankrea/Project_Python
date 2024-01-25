"""
常见转换语句
当浮点数转换成整数时，会丢失精度
int()   转换成整数类型
float() 转换成小数(浮点数)类型
str()   转换成字符串
"""
# 将数字类型转换为字符串
a =str(10086)
# 将字符串转换成数字
b =int("10000")
# 将数字转换成浮点数
c = float(100)
print(type(a),a)
print(type(b),b)
print(type(c),c)