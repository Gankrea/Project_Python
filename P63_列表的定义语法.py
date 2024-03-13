''''
列表的定义
列表内的每一个数据，都称之为元素
以[]作为标识，每个元素之间用 , 隔开

定义空列表
    变量名 = []
    变量名 = list()

容器内的每一份数据，都称之为元素
'''
# 字面量
['元素1', '元素2', '等......']

# 定义变量
name = ['张三', '李四', '王五', '老六']
print(name)
print(type(name))

# 支持嵌套
my_list = [[1, 2, 'python'], ['True', '数据']]
print(my_list)
print(type(my_list))
