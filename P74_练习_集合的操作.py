my_list = ["黑马程序员", "博客", "黑马程序员", "博客", "itheima", "best",
           "itheima", "itcase", "itcase"]

# 定义一个空集合
sky = set()

# 通过for循环遍历列表
for i in my_list:

    # 在for循环中将列表的元素添加至集合
    sky.add(i)
print(my_list)
# 最终得到元素去重后的集合对象,并打印输印
print(sky)
