# 定义外层循环的控制变量
i = 1
while i <= 9:

    j = 1
# 控制内层循环的控制变量
    while j <= i:
        print(f"{j}*{i}={i * j}\t",end='')
        j += 1
    i += 1
    print()