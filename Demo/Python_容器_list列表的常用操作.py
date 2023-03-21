"""
list列表的常用操作

功能特点:
        -  可以容纳多个数据(上限是2**63-1)
        -  可以容纳不同类型的数据(混装)
        -  数据是有序存储的(有下标序号)
        -  允许重复数据存在
        -  可以修改(增加或删除等)
"""
mylist = ["itheima", "itcast", "python"]
# 1.1 查找某元素在列表内的下标索引
# 语法: 列表.index(元素)
index = mylist.index("itheima")
print(f"iteheima在列表中的下标索引是: {index}")

# 1.2 如果被查找的元素不存在,会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下标索引是: {index}")

# 2. 修改特定下标索引的值
# 语法: 列表[下标] = 值
mylist[0] = "传智教育"
print(f"列表的元素被修改后,结果是: {mylist}")

# 3. 在指定下标位置插入新元素
# 语法: 列表insert(下标,元素)
mylist.insert(1, "best")
print(f"列表元素插入后,结果是: {mylist}")

# 4. 在列表尾部追加'''单个'''新元素
# 语法: 列表.append(元素)
mylist.append("黑马程序员")
print(f"列表在追加了元素后,结果是: {mylist}")

# 5. 在列表的尾部追加个'''一批'''的元素
# 语法: 列表.extend(其他数据容器)
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加了一个新的列表后,结果是:{mylist}")

# 6. 删除指定下标索引的元素(2种方式)
# 语法1: del列表[下标]        这个仅仅只是删除
mylist = ["itheima", "itcast", "python"]
del mylist[2]
print(f"列表删除元素后结果是: {mylist}")
# 语法2: 列表pop法           这个不仅可以把元素删掉,还可以把删掉的元素作为返回值去得到
mylist = ["itheima", "itcast", "python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容是: {mylist},取出的元素是: {element}")

# 7. 删除某元素在列表中的第一个匹配项
# 语法: 列表.remove(元素)
mylist = ["itheima", "itcast", "itheima", "itcast", "python"]
mylist.remove("itheima")
print(f"通过remove方法移除元素后,列表的结果是: {mylist}")  # remove方法会删掉从右往左数第一个匹配的值

# 8. 清空列表
# 语法: 列表.clear()
mylist.clear()
print(f"列表被清空了,结果是: {mylist}")

# 9. 统计列表内某些元素的数量
# 语法: 列表count(元素)
mylist = ["itheima", "itcast", "itheima", "itcast", "python"]
count = mylist.count("itheima")
print(f"列表中itheima的数量是: {count}")

# 10. 统计列表中全部的元素的数量
# 语法: len(列表)
mylist = ["itheima", "itcast", "itheima", "itcast", "python"]
count = len(mylist)
print(f"列表的元素数量总共有: {count} 个")

# 练习
# 定义一组列表
stu = [21,25,21,23,22,20]
print(f"定义后的学生年龄: {stu}")
# 增加到尾部操作       append
stu.append(31)
print(f"增加后这批学生的年龄: {stu}")
# 增加一组列表到尾部操作      extend
stu2 = [29,33,30]
stu.extend(stu2)
print(f"增加完新列表后这批学生的年龄: {stu}")
# 正面取第一个数据
num1 = stu[0]
print(f"取出第一个元素为: {num1}")
# 取出最后一个元素的操作
num2 = stu[-1]
print(f"取出最后一个元素为: {num2}")
# 找到元素31的下标位置  index
stu_index = stu.index(31)
print(f"元素31在列表的下标位置是: {stu_index}")
print(f"最后列表的内容是: {stu}")



