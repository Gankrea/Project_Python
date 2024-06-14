str_soumt = "itheima itcast boxuegu"
# 统计字符串内有多少个 it 字符
sum = str_soumt.count('it')
print(f"字符串 {str_soumt} 内有 {sum} 个字符")

# 将字符串内的空格替换为 |
newstr_sun = str_soumt.replace(' ','|')
print(f"新字符串是：",(newstr_sun,))

# 按照 | 分割字符串，得到列表
list_sonr = newstr_sun.split("|")
print(list_sonr)
