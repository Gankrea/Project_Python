# 通过外层循环控制行数
for i in range(1, 10):
    # 内层循环控制每行的数据
    for j in range(1, i+1):
        print(f"{i}*{j}={i * j},", end='')
    print()