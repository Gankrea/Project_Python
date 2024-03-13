list1 = [1,23,4,5,23,16,76,43,42,]
# 用while循环遍历列表
# 定义一个变量记录列表的下标
index = 0
# 下标小于列表的元素
# len()表示列表的长度
print("--------while循环---------")
while index < len(list1):
    # 打印
    print(list1[index])
    # 每次循环，index都+1
    index+=1

# 用for循环遍历
print("--------for循环---------")
for tran in list1:
    print(tran)