"""
字符串是字符的容器,一个字符串可以存放任意数量的字符
和其它容器如:列表、元组一样,字符串也可以通过下标进行访问
    通过下标获取特定位置字符
注意
    字符串容器也是一个无法修改的数据容器
"""
# 定义一个字符串容器
str_name = "itheima"

# 从前向后,下标从0开始
print(str_name[0]) # 结果i

# 从后向前,下标从-1开始
print(str_name[-1]) # 结果a

"""
查找特定字符串的下标索引值
语法
    字符集.index=(字符串)
"""

str_soun = "computer","banana","apple"

print(str_soun.index("banana")) # 1

"""
字符串的替换
语法:字符串.replace(字符串1,字符串2)
功能:将字符串内的全部:字符串1,替换为字符串2
注意:不是修改字符串本身,而是得到了一个新字符串
"""
str_teapr ="sotren"

newstr_teapr = str_teapr.replace("sotren","itheima")
print(newstr_teapr)

"""
字符串的分割
语法:字符串.split(分隔符字符串)
功能:按照指定的分隔符字符串,将字符串划分为多个字符串,并存人列表对象中
注意:字符串本身不变,而是得到了一个列表对象
"""
str_tyune = "itheima head red backgroundcolor"
# 要注意空格
newstr_sobtye = str_tyune.split(" ")
print(newstr_sobtye)

str_sont ="itheima head"
som= str_sont[8]
# 字符串下标不包含空格内容
print(som)