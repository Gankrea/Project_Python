name = "月薪过万"
age1 = 100
miss1 = "学IT就来 %s" %age1
print(miss1)
# 使用占位符就可以把非字符串的类型拼接到一起
"""
若有多个变量占位，则需要用()括起来，也需要多个占位符
且会按照占位的顺序
"""
age2 = 456
age3 =123
# %表示 占位符   s表示把变量变成字符串然后放入占位符中
# %s 把内容转换成字符串，放入占位符
# %d 把内容转换成整数，放入占位符
# %f 把内容转换成浮点数，放入占位符
miss2 = "你是 %s 我是 %s" % (age2,age3)
print(miss2)
