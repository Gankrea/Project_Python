# 数一数有多少字母 a

name = "itheima is a brand of itcast"
# 累加计数
num = 0
for i in name:
    if i == "a":
        num += 1
print(f"一共有{num}个字母a")
