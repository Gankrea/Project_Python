# 定义求和变量
num = 0
for i in range(1,101):
    if i%2==0:
        num+=num
print(f"1-100的偶数和是{num}")