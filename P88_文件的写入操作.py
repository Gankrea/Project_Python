import time

# 文本路径 打开模式 字符编码
# r 只读  w 写入
f = open("D:/Project_Python/P88_文件写入操作.txt", "w", encoding="utf-8")
# write 写入内容
f.write("这是写入的内容11111")

# 把内存的数据写入硬盘中
f.flush()
print(12345)

# 程序暂停3秒
time.sleep(3)

print(54321)
# 关闭文件
f.close()
"""
直接调用write,内容并未真正写入文件,而是会积攒在程序的内存中,称之为缓冲区
当调用flush的时候,内容会真正写入文件
这样做是避免频繁的操作硬盘,导致效率下降(攒一堆,一次性写磁盘)

打开模式
    w 若文件不存在，将会创建
    当文件存在时，会把内容清空，再把内容写入

flush 把缓冲区的内容写入文件中
close 内置了flush功能

write()，写入内容
flush()，刷新内容到硬盘中

"""