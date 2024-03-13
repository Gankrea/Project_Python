"""
方法：
class 方法名(self,形参1，形参2.....)
    def 函数名(形参):
        代码段
        return 返回值
函数：
def 函数名(形参):
    代码段
    return 返回值
"""


"""
插入元素
列表.insert(下标,元素)
在指定的下标位置，插入指定的元素
"""
trans = ['1','2','3']
trans.insert(3,'4')
print("--------插入元素--------")
print(trans)
"""
追加元素
列表.append(元素)
将指定元素追加到列表的末尾
"""
tsyrn = ['sound','tran','fla','49']
print("--------追加1，单个--------")
son = tsyrn.append('追加')
print(tsyrn)
"""
追加一堆元素
列表.extend(数据容器)
将其它数据容器的内容取出,依次追加到列表尾部
"""
soty = ['0483','983','2312']
soty.extend(['True','王五',3])
print("--------追加2，一堆元素--------")
print(soty)

"""
删除
del 列表[下标]
既是删除又是提取操作
列表 pop[下标]
"""
strop = ['43','93','12','True','王五',]
print("--------删除--------")
del strop[0]
print(f"先删除0号元素,删除后剩下的列表是{strop}")
# 变量 = 列表.pop(下标)
stroe =  strop.pop(3)
print("--------删除并提取--------")
print(f"提取的值是：{stroe}，提取后的列表是{strop}")

print("--------删除某元素第一匹配项--------")
kopre = [1,2,3,2,3,4,4]
#   列表.remoer(元素)
# 把列表中第一个与元素相匹配的列表的元素删除
kopre.remove(3)
print(f"删除第一匹配项后的列表结果是{kopre}")
"""
清空列表
列表.clear()
"""
styu = [1,2,3,4,5,6,7,8]
styu.clear()
print(f"删除所有元素后，列表内容为：{styu}")

"""
修改
列表[元素的下标] = 修改后的元素 
"""
print("--------修改--------")
trean1 = ['26','2000','元素2','张三']
trean1[3]="老六"
tera = trean1[3]
print(tera)
"""
查找指定元素的下标
变量 =(赋值) 列表.index("元素的名称")
"""
print("--------查找元素下标--------")
tram = trean1.index("元素2")
print(f"元素的下标是：{tram}")  # 2
"""
统计某元素在列表内的数量
列表.count(元素)
"""
print("--------统计--------")
styre = [1,2,3,4,5,3,4,1,312,312,34,21,]
son = styre.count(3)
print(f"元素3在列表中有{son}个")
# 函数
def add(x,y):
    return x+y
# 函数的调用
tern = add(8,2)


# 方法
class adde():
    def arenrt(self,x,y):
        return x+y
# 方法的调用
stud = adde()

# 变量 (=)赋值 类.函数
num = stud.arenrt(1,20)

