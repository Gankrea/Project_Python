import random
# 工资池
salary = 10000

for staff in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{staff},绩效分为{num},不发工资")
        continue
    else:
        salary -= 1000
        print(f"员工{staff},绩效为{num},准予发放，工资池还剩{salary}")
    if salary == 0:
        print("工资发完了")
        break
