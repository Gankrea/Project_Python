list1 = [21, 25, 21, 23, 22, 20]
list1.append(31)
print(f"追加后的列表是{list1}")
list1.extend([29,33,30])
print(f"追加一堆元素后，列表状态为：{list1}")
# 取出第一个元素
one = list1.pop(0)
print(f"第一个元素{one}取出后，列表有{list1}")
# 取出末尾的第一个元素
two = list1.pop(-1)
print(f"最后一个元素{two}取出后，列表有{list1}")
# 查找元素的下标
dex = list1.index(31)
print(f"元素31在列表的下标是{dex}")