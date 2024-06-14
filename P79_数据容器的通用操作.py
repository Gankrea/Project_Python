"""
len(容器)
    统计容器的元素个数

max_1(容器)
    统计容器的最大元素

min(容器)
    统计容器的最小元素

通用转换
list()  表列为换转器容定给将

str()   将给定容器转换为字符串

tuple() 将给定容器转换为元组

set()   将给定容器转换为集合

sorted(容器, [reverse=True])
是否倒序 是True  否False
注意：排序后结果会变成列表对象
"""

# 列表
my_list = [1,2,3,4,5,6,7,8,9]

# 元组
my_tuple = ()

# 字典
my_dict = {}

# 字符串
my_str = ""

# 集合
my_set = {}

let = len(my_list)
max_1 = max(my_list)
man_1 = min(my_list)
print(f"列表长度为{let}")
print(f"元素最大为{max_1}")
print(f"元素最小为{man_1}")
