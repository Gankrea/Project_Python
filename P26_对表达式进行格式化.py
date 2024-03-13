"""
表达式的概念:一条具有明确执行结果的代码语句
    等号右侧的都是表达式，因为它们有具体的结果，结果赋值给了等号左边的变量
    name = "张三" age = 17+1
"""
name = "张三"
print("我的名字是：%s" %{name})
# 这种方式无需定义变量，直接把表达式写入即可
print("我的名字是：%s" %{"张三"})

# 这种方式无需定义变量，直接把表达式写入即可
print("1*1的结果是：%d" %(1*1))
print(f"1*2的结果是：{1*2}")
print("字符串的类型名是：%s" %type("字符串"))
