"""
集合(去重)不支持重复元素
    可对数据进行去重处理
语法
   定义集合字面量
   {元素,元素2,元素3,......}
   定义集合变量
    变量名称 = {元素,元素2,元素3,......}
    定义空集合
    变量名称 = set()

不支持下标索引

添加新元素
    集合.add("需要添加的元素")

移除元素
    集合.remove("需要删除的元素")

随机取出一个元素
    有返回值
    变量名 = 集合.pop()

清空集合
    集合.clear()

差集
    集合.difference(集合)
    取差集后，原集合内容不变

消除2个集合的差集
    集合1.difference_update(集合2)

2个集合合并，得到新集合，且原集合内容不变
    集合3 = 集合1.unior(集合2)

统计集合元素的数量
    num = len.(集合)

集合的遍历
    集合不支持下标索引，所以不能用while循环，但可用for循环
"""
"""
添加元素
"""
sount = {"python", "13579"}
sount.add("heima")
print(sount)

"""
删除元素
"""
sount.remove("python")
print(sount)

"""
取差集
"""
set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 表示在set1里面取出和set2不同的元素
set3 = set1.difference(set2)
print(set3)

"""
消除2个集合的差集
"""
set10 = {1, 2, 3}
set20 = {1, 5, 6}
# 表示在set10里面消除和set20相同的元素
set10.difference_update(set20)
print(set10)
print(set20)

"""
集合合并
    合并两集合，得到新集合。原集合内容不变，且不重复元素
"""
set10 = {1, 2, 3}
set20 = {1, 5, 6}
set30 = set10.union(set20)
print(set30)

# 统计集合的元素数量
setom = {1, 2, 2, 4, 5, 6, 7, 8, 8}
suntew = len(setom)
print(f"集合是去重的，所以 suntew 集合内有{suntew}个元素")

# 集合的遍历
set135 = {1, 2, 3, 76, 98, 9}
for i in set135:
    print(f"集合set135内的元素有{i}")
