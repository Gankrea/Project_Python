
# 读取源文件
f1 = open("D:/Project_Python/P90_练习_文件操作的综合案例.txt","r",encoding="utf-8")

# 准备写入另一个文件
f2 = open("D:/Project_Python/P90_练习_文件操作的综合案例.txt.bak","w",encoding="utf-8")
# 读取文件内容
for line in f1:
    #
    line = line.strip()
    # 判断文件内容，满足条件的写出
    if line.split(",")[4]=="测试":
       continue # 跳过本次循环，进行下一轮
    # 把内容写出
    f2.write(line)
    # 手动换行操作
    f2.write("\n")


# 缓冲写入
f1.close()
# 关闭文件
f2.close()
