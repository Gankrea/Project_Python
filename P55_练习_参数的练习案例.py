def styron(num):
    if num > 37.5:
        print(f"欢迎来到>>>>>>>>>> \n 体温检测中，你的体温是{num},需要隔离")
    else:
        print(f"欢迎来到>>>>>>>>>> \n 体温检测中，你的体温是{num},体温正常")
# 调用并传入实参
styron(int(input("请输入你的体温：")))

