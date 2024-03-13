a =10
if int(input("输入猜想的数：")) == a:
    print("恭喜你猜对了")
elif int(input("猜错了，请再猜一次："))==a:
    print("恭喜你猜对了")
elif int(input("猜错了，还剩最后一次机会："))==a:
    print("恭喜你猜对了")
else:
    print("机会已经用完，失败了")