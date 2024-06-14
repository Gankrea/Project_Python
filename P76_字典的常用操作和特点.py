"""
新增元素 语法：
    字典名[key] = value
更新元素 语法：
    字典名[key] = value,结果:字典被修改,元素被更新
    注意:字典Key不可以重复,所以对已存在的Key执行上述操作,就是更新Value值

"""
my_dict = {"数学": 100, "语文": 88, "英语": 78}
# 修改
print(f"修改后的结果是{my_dict}")

# 删除
my_dict.pop("数学")
print(f"删除后的结果是{my_dict}")

# 清空
my_dict.clear()
print(my_dict)

# 获取全部的key
my_dict = {"数学": 10, "语文": 88, "英语": 78}
keys = my_dict.keys()
print(keys)

# 遍历字典
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计元素数量
num = len(my_dict)
print(f"字典中元素有{num}个")
