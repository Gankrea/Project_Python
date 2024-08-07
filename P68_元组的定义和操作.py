"""
元组的特点：
    元组一旦定义完成，就无法修改
    且元组内的元素是不受限的
定义空元组
    变量名 = ()
    变量名 = tuple()
"""
# 定义元组变量
t1 = ('元素1', 345, True,)
print(type(t1))

t10 = ("hello")  # 字符串
t11 = ("hello",)  # 元组
"""
若定义单个元素的元组，需要后面添加逗号。否则会变成数据类型
"""
print(f"t10的数据类型是{type(t10)},内容是{t10}")
print(f"t11的数据类型是{type(t11)},内容是{t11}")

# 元组的嵌套
t800 = ((1, 2, 3), (4, 5, 6, 7, 8))
# 取出元组内的元素(使用下标)
toun = t800[1][2]
print(toun)
"""
元组的操作
    index()查找某个数据，若存在则返回对应的下标，否则报错
    count()统计某个数据在该元组内出现的次数
    len(元组)统计元组内的元素个数
"""
# 定义元组
t1000 = ("直行", "左转", "右转", "掉头", "左转",)
tson = t1000.index("右转")
# index() 返回元素索引的下标
print(f"在元组t1000中，右转下标是：{tson}")
# count() 统计某个数据在该元组内出现的次数
sum = t1000.count("左转")
print(f"在元组t1000中，左转有：{tson}个")
# len(元组)统计元组内的元组个数
tson = ("禁止通行","小电驴","小轿车")
std = len(tson)
print(f"在{tson}元组内有{std}个元素")

# 元组内元素的遍历

for i in tson:
    print(f"用for循环遍历元组，有{i}")

inst = 0
while inst < len(tson):
    print(f"用while循环遍历元组，有{inst}")
    inst+=1

# 该元组内包含列表(可以修改)
t212 = ("we",["日奈","亚子"],"true")
print(f"未经修改的列表{t212}")
# 修改元组内的列表元素
t212[1][1] = "sensei"
t212[1][0] = "日奈"
print(f"经过修改后元组内容是{t212}")
