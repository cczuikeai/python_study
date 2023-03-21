"""
 Python中的容器相当于Java中数组或集合的概念

 格式:
    # 字面量
    [元素1,元素2,元素3...]
    # 定义变量
    变量名称 = [元素1,元素2,元素3...]
    # 定义空列表
    变量名称 = []
    变量名称 = list()
"""

# 定义一个基础的列表
my_list = ["iteheima", "itcast", "python"]
print(my_list)
print(type(my_list))

my_list = ["iteheima", 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))

# 通过下标索引取出对应位置的数据
my_list = ["Tom","Lily","Rose"]
# 列表[下标索引],从前往后,从0开始,每次+1       从后往前,是从-1开始,每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 通过下标索引取出数据(倒序取出)
print(my_list[-3])
print(my_list[-2])
print(my_list[-1])

# 取出嵌套列表的元素
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])