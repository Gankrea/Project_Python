"""
列表的下标
    从左到右，0开始
或者
    从右往左，-1开始
注意索引的取值范围，超出范围会报错
"""
# 从左到右，0开始
name1 = ['张三', '李四', '王五', ]
print(name1[0])
print(name1[1])
print(name1[2])

print("------反向索引------")
# 从右往左，-1开始
name2 = ['张三', '李四', '王五', ]
print(name2[-1])
print(name2[-2])
print(name2[-3])

print("------嵌套列表------")
# 嵌套列表
name_rgb = [['梓', 'Java'], ['Go语言', 'C语言', 'Python'], ['Php', 'Html', 'CSS', 'JavaScript']]
print(name_rgb[0][0])
print(name_rgb[1][2])
print(name_rgb[2][3])
