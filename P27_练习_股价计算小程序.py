# 公司名
name = "悠星娱乐"
# 股价
price = 182
# 股票代码
# 注意！数字不能以0开头，否则会报错，所以要使用字符串类型定义
code = "0010824"
# 增长系数（浮点型）
factor = 1.2
# 增长天数
days = 8
max = factor*factor*days*price
print(f"公司：{name},股票代码：{code}，当前股价：{price}")
print("每日增长系数是：%.1f 经过%d天的增长后，股价达到了:%.2f" %(factor,days,max))
