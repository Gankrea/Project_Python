"""
影响范围只在该循环内部
continue
跳过本次循环，直接进入下一次循环
可用于for和while循环，效果一致

break
直接结束该本层的循环
"""
# for i in range(1,5):
#     print("语句1")
#     continue       跳过本次循环
#     print("语句2")  该语句不执行

for j in range(1, 4):
    print("语句1")
    for u in range(1, 4):
        print("语句2")
        break  # 直接结束掉本层循环，执行下一步操作(语句4)
        print("语句3")    # 该行代码无法执行
    print("语句4")
