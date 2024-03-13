import random

num = random.randint(1, 100)

# 总共测试多少次
i = 0

# 使用布尔值赋值给一个变量，当猜中后，改变变量的布尔值
flag = True
print(num)

# 条件 sum!=num 也可以
while flag:
    i += 1
    sum = int(input("请输入你要猜的数字："))
    if sum == num:
        print("恭喜你猜对了")
        # 由于布尔值之间不能相互赋值，所以需要一个变量
        # True = False 是无法相互赋值的
        flag = False
    elif sum > num:
        print("大了")
    else:
        print("小了")
print(f"总共猜了：{i}次")
