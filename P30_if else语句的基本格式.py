"""
if语句的基本格式
if 要判断的条件 :
[][][][] 条件成立时所执行的语句

注意：判断的结果是布尔(bool)类型
归属于if语句的代码块，要在前方填充4格空格缩进
不要忘记判断条件后面的冒号(:)

在else后，不需要判断条件
也同样需要4个空格做缩进
"""
age = input("请输入你的年龄：")

if int(age) >= 18:
    print("你已经成年")
    print("即将步入大学生活")
else:
    print("你还未成年")

print("时间过的真快")