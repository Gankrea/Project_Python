# range语句
"""
语法1
range(num)
从0开始，到num结束的数字 不包含num本身
例：range(5)取得的数字是[0,1,2,3,4]
"""
for i1 in range(6):
    print(i1)
"""
语法2
range(num1,num2)
获得一个从num1开始，到num2结束的数字序列 不包含num2
例：range(5,10)取得的数字是[5,6,7,8,9]
"""
for i2 in range(3,10):
    print(i2)
"""
语法3(添加步长)
range(num1,num2,step)
获得一个从num1开始，到num2结束的数字序列 不包含num2
数字之间的步长，以step为准（默认为1）
例：range(5,10,2)取得的数是[5,7,9]
"""
for i3 in range(10,20,5):
    # 注意！不包含num2
    print(i3)

"""
练习
num = 0
for i in range(1, 100):
    if i % 2 == 0:
        num += 1
print(f"1-100范围内(不包含100)，有{num}个偶数")

"""