"""print("---------------主菜单---------------\n"
      "欢迎使用ATM，请选择你需要的操作\n"
      "查询余额    \t[输入1]\n"
      "存款       \t[输入2]\n"
      "取款       \t[输入3]\n"
      "退出       \t[输入4]\n"
      "------------------")

num = int(input("请输入你想要的操作："))


# 定义全局变量 存款
money = 10000

# 查询存款函数
def trean_1():
    print(f"你的余额为：{money}")

if num == 1:
   trean_1()


def tream_2():
    mone = int(input("请输入你要存的余额:"))
    global money
    money+=mone
    return money


if num ==2:
    tream_2()
    print(f"成功，账户还有:{money}元")

# 取款操作函数
def ter2an_2():
    # 把money局部变量设置成全局变量并返回
    global money
    x = int(input("请输入你要取款的金额"))
    money-=x
    return money

if num == 3:
   newmon = ter2an_2()
   print(f"成功，你的账户余额为{newmon}元")

# 退出操作函数
def ex1it_1():
    print("程序已退出")
if num ==4 or num>4 or num<1:
    ex1it_1()
"""
# 定义全局变量 余额
money = 88888

# 定义查询函数
def cx_():
    print(f"余额还有{money}元")

# 定义存款函数
def ck_(c):
    global money

    money+=c
    print(f"存款{c}元成功")
    cx_()
    return money
# 取款函数
def qk_(q):
    global money
    money-=q
    print(f"取款{c}元成功")
    cx_()
    return money
# 主菜单函数
print("---------------主菜单---------------\n"
      "欢迎使用ATM，请选择你需要的操作\n"
      "查询余额    \t[输入1]\n"
      "存款       \t[输入2]\n"
      "取款       \t[输入3]\n"
      "退出       \t[输入4]\n"
      "------------------")

while  True:
    num = int(input("请输入你想要的操作："))
    if num == 4:
        print("程序已退出")
        break
    elif num == 1:
        cx_()
    elif num == 2:
        c = int(input("请输入你要存入的金额"))
        ck_(c)

    elif num == 3:
        q = int(input("请输入你要取款的金额"))
        qk_(q)
