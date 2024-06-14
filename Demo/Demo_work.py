array1 = [1, "黑马", 3, [54], 5]
print(type(array1))

# 元素个数
sum=0

# 元素类型
for i in array1:
    sum+=1
    ston =type(i)
    print("%d 数组内的元素类型是",ston )


print("元素的个数有："+ sum+"个")
