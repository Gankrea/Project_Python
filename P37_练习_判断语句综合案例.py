"""
import random

num = random.randint(1, 10)
print("答案是", num)
ad1 = int(input("请输入(第一次)："))
if ad1 == num:
    print("恭喜你猜中了")
else:
    if ad1 > num:
        print("猜大了")
    else:
        print("猜小了")
    ad2 = int(input("请输入(第二次)："))
    if ad2 == num:
        print("恭喜你猜中了")
    else:
        if ad2 > num:
            print("猜大了")
        else:
            print("猜小了")

    ad3 = int(input("请输入(第三次)："))
    if ad3 == num:
        print("恭喜你猜中了")
    else:
        print("猜错了，机会已用完")
"""
# 产生随机数代码
import random

num = random.randint(1, 10)
print("开始猜数字游戏，范围是1-10的整数")
print("答案是", num)
ad1 = int(input("请输入(第一次)："))
if ad1 < num:
    print("猜小了")
    ad2 = int(input("请输入(第二次)："))
    if ad2 < num:
        print("猜小了")
        ad3 = int(input("请输入(第三次)："))
        if ad3 != num:
            print("猜错了，机会已经用光")
        elif ad3 == num:
            print("猜中了")
    elif ad2 > num:
        print("猜大了")
        ad3 = int(input("请输入(第三次)："))
        if ad3 != num:
            print("猜错了，机会已经用光")
        elif ad3 == num:
            print("猜中了")
    else:
        print("恭喜你猜中了")
elif ad1 > num:
    print("猜大了")
    ad2 = int(input("请输入(第二次)："))
    if ad2 < num:
        print("猜小了")
        ad3 = int(input("请输入(第三次)："))
        if ad3 != num:
            print("猜错了，机会已经用光")
        elif ad3 == num:
            print("猜中了")
    elif ad2 > num:
        print("猜大了")
        ad3 = int(input("请输入(第三次)："))
        if ad3 != num:
            print("猜错了，机会已经用光")
        elif ad3 == num:
            print("猜中了")
    else:
        print("恭喜你猜中了")
else:
    print("恭喜你猜中了")
