"""
列表的遍历
"""


# while循环遍历列表
def list_while_func():
    """
    使用while循环遍历列表的函数
    :return: None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    # 循环变量通过下标索引来控制,默认是0
    # 每一次循环将下表索引变量+1
    # 循环条件: 下标索引变量 < 列表的元素数量
    index = 0  # 初始值为0
    while index < len(my_list):
        # 通过index变量取出相应下标的元素
        element = my_list[index]
        print(f"列表的元素: {element}")

        # 最重要的一步,将循环变量index每次循环+1
        index += 1


list_while_func()

def list_for_function():
    """
    使用for循环遍历列表的函数
    :return: None
    """
    my_list = [1,2,3,4,5]
    for element in my_list:
        print(f"列表的元素有: {element}")

list_for_function()

# 使用while循环遍历
my_list1 = [1,2,3,4,5,6,7,8,9,10]   # 定义初始列表
my_list2 = []   # 提前定义新的列表
index = 0   # 定义好下标的初始值为0
while index < len(my_list1):    # 循环条件式,下标小于列表的元素的数量
    if my_list1[index] % 2 == 0:    # 判断如果初始列表的元素刚好整除2的时候,进入下一步操作
        my_list2.append(my_list1[index])    # 用append函数,把初始列表里符合要求的数据添加到新的列表
    index += 1  # 循环变量,每次循环结束加1直到不符合循环条件

print(f"通过while循环,从列表: {my_list1}中取出偶数,组成新列表: {my_list2}")

# 使用for循环遍历
my_list1 = [1,2,3,4,5,6,7,8,9,10]
my_list2 = []
for i in my_list1:  # 运用for循环将初始列表的数据遍历给i
    if i % 2 == 0:  # 判断数据i是否整除2
        my_list2.append(i)  # 如果是整除,就把i添加到新列表中去
print(f"通过while循环,从列表: {my_list1}中取出偶数,组成新列表: {my_list2}")

