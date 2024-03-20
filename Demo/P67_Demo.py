# 原始列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定义一个装奇数的空列表
list100 = []
# i 表示列表里面的元素
for i in list1:
    if i % 2 != 0:
        # 当符合条件时，则添加到空的列表中
        list100.append(i)
print(f"通过for循环遍历了{list1}后，\n"
      f"取出的奇数列表是{list100}")

# 定义一个空变量
num = 0
# 定义一个装偶数的空列表
list200 = []

while num < len(list1):
    if list1[num] % 2 == 0:
        list200.append(list1[num])
    num += 1
print(f"取出的偶数列表是{list200}")