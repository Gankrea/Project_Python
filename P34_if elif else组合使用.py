"""
常在多条件的判断
if
elif
elif
else
注意：if,elif,else都是同级的关系，没有缩进

从上到下进行条件判断，如果if条件满足，elif就不会执行
"""
"""
height = int(input("请输入你的身高(cm)："))
vip =int(input("你是否有VIP？(0-1)："))
可以直接把输入语句写入条件判断中，以使代码更加简短
"""
# 免费游玩判断
if int(input("请输入你的身高(cm)：")) <= 120:
    print("检测到你是儿童，可免费游玩")
elif int(input("你是否有VIP？(0-1)："))==1:
    print("尊贵的VIP用户，您可以免费游玩")
# 付费游玩判断
else:
    print("需要购票游玩")