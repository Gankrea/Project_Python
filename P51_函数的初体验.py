# 函数是组织好的，可重复使用的，用来实现特定功能的代码段
# 好处是可重复利用，减少重复代码，提高开发效率
"""
字符串长度统计
关键字 len()

name ="heima"
sum = len(name)
print(sum)  # 5

"""
# 统计字符串的长度，不使用内置函数len()
name1 = "python"
name2 = "itheima"
name3 = "int"

sum = 0
for i in name1:
    sum += 1
print(f"字符串{name1}的长度是{sum}")
sum = 0
for i in name2:
    sum += 1
print(f"字符串{name2}的长度是{sum}")
sum = 0
for i in name3:
    sum += 1
print(f"字符串{name3}的长度是{sum}")

# 自己定义新的字符串长度统计
def my_len(data):
    count = 0
    for i in data:
        count+=1
    print(f"字符串{data}的长度是{count}")
my_len(name1)
my_len(name2)
my_len(name3)