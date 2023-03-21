"""
 集合的特性:
    - 无序
        - 因为无序,所有不支持下标索引访问,但是允许你修改
    - 不可重复
 集合的语法:
    - 字面量
        - {元素,元素,元素...}
    - 集合变量
        - 变量名称 = {元素,元素,元素...}
    - 空集合
        - 变量名称 = set()
"""

# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()  # 定义空集合
print(f"my_set的内容是: {my_set},类型是: {type(my_set)}")
print(f"my_set_empty的内容是: {my_set_empty},类型是: {type(my_set_empty)}")

# 添加新元素     集合.add()
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加后的结果是: {my_set}")

# 移出元素      集合.remove()
my_set.remove("黑马程序员")
print(f"my_set移出以后得结果是: {my_set}")

# 随机取出一个元素      集合.pop()
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()
print(f"集合被取出元素是: '{element}',取出元素后的结果是: {my_set}")

# 清空集合      集合.clear()
my_set.clear()
print(f"集合被清空了,结果是: {my_set}")

# 取2个集合的差集
# 语法: 集合1.difference(集合2)   取出来的是1里面有,2里面没有的东西
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)  # 取的是1里面有2里面没有的东西
print(f"取出差集后的结果: {set3}")
print(f"取差集后,原来set1 的内容是: {set1}")
print(f"取差集后,原来set2 的内容是: {set2}")

# 消除2个集合的差集             消除的是和集合2一样的数字
# 语法: 集合1.difference_update(集合2)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)  # 消除的和集合2一样的东西
print(f"消除差集后,原来set1 的内容是: {set1}")
print(f"消除差集后,原来set2 的内容是: {set2}")

# 2个集合合并        将集合1和集合2组合成一个新集合,1和2集合保持不变
# 语法: 集合1.union(集合2)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)  # 消除的和集合2一样的东西
print(f"合并成的新集合为: {set3}")
print(f"合并集合后,原来set1 的内容是: {set1}")
print(f"合并集合后,原来set2 的内容是: {set2}")

# 统计集合元素数量      len(集合)
set1 = {1, 2, 3, 4, 5, 6, 7}
num = len(set1)
print(f"集合内的元素数量有:{num}个")

# 集合的遍历
# 集合不支持下标索引,所以不支持while循环
# 可以用for循环
set1 = {1,34,667,2341,23}
for i in set1:
    print(f"集合的元素有: {i}")

print("-----------------------------------")
# 练习
my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]

# 定义一个空集合   set()
my_list_empty = set()

# 通过for循环来遍历列表
for element in my_list:
    print(f"集合的元素有: {element}")
    my_list_empty.add(element)
print(f"有列表: {my_list}, 存入集合后结果为: {my_list_empty}")


