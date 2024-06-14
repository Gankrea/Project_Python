# 打开文件，只读方式打开
f = open("D:\Project_Python\P87_文本测试文件.txt", "r", encoding="UTF-8")

# 方法一
# content = f.read()
# count = content.count("itheima")
#
# print(f"itheima在文件中出现了{count}次")


# 方法二
# 计数变量
count = 0
for line in f:
    # 去除开头结尾空格和换行符
    line = line.strip()

    words = line.split(' ')
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima出现的次数是：{count}")

