sound = ('heima',11,['play games','movie'])
# 查询年龄的下标
sp = sound.index(11)
print(f"年龄的下标是{sp}")

# 查询姓名
stron = sound[0]
print(f"姓名是{stron}")

# 删除爱好
del sound[2][0]
print(f"删除后的元组内容是{sound}")

# 添加爱好
# 元组[下标](列表).append()
sound[2].append("play student")
print(f"添加后的元组内容是{sound}")