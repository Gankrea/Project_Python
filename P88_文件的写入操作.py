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
