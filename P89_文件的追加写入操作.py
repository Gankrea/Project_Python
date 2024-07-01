"""
使用 a 模式打开文件
    文件不存在会创建文件
    文件存在，会在原有内容后面继续写入
    可以使用 \n 来写出换行符

"""

f = open("D:/Project_Python/P89_文件的追加写入操作.txt","a", encoding="utf-8")
# 内容写入缓冲区
f.write("黑马程序员\n空崎日奈")
# 把缓冲区的内容写入到文件中
f.flush()
# 关闭文件
f.close()