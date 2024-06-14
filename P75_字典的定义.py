"""
作用：通过字典找到其所属的信息
    且不允许重复，若遇到相同的key，则后面的会把前面的给覆盖掉
    也无法使用下表索引

# 定义
{
    # 键值对
    key1:value1,
    key2:value2,
    key3:value3,
}

# 定义字典变量
my_dict = {key: value, key: value,}

# 定义空字典
my_dict = {}
my_dict = dict()

字典的注意事项
    键值对的Key和Value可以是任意类型(Key不可为字典)
    字典内Key不允许重复,重复添加等同于覆盖原有数
"""
my_dict = {
    "姚蒙": "没亩",
    "悠星": "破产",
    "sky": "天空",
}
print(f"my_dict的数据类型是{type(my_dict)}")
# 用key值获取对应的value
banana = my_dict["sky"]
print(banana)

# 字典的嵌套
apple = {
    "姓名1": {
        "语文": 87,
        "数学": 65,
    },
    "姓名2": {
        "语文": 78,
        "数学": 65,
    },
    "姓名3": {
        "语文": 87,
        "数学": 65,
    },
}
print(apple["姓名2"])
# 可详细取出value值
print(apple["姓名3"]["语文"])