"""
 - 元组的定义和列表一样,可以封装多个,不同类型的元素
 - 最大的不同点在于元组一旦完成,就不可修改

 定义元组使用小括号,数据间用逗号隔开
 - 定义元组字面量
 (元素1,元素2,元素3...)
 - 定义元组变量
 变量名称 = (元素,元素,元素...)
 - 定义空元组
 变量名称 = ()  # 方式1
 变量名称 = tuple() # 方式2
"""
# 定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是: {type(t1)}, 内容是: {t1}")
print(f"t2的类型是: {type(t2)}, 内容是: {t2}")
print(f"t3的类型是: {type(t3)}, 内容是: {t3}")

# 定义单个元素的元组
# 当小括号里只有一个元素的时候,如果不写逗号,就不是元组了
t4 = ("hello", )
print(f"t4的类型是: {type(t4)}, 内容是: {t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是: {type(t5)}, 内容是: {t5}")

# 下标索引去取出内容
num= t5[1][2]
print(f"从嵌套元组中取出的数据是: {num}")

# 元组的操作: index查找方法
t6 = ("传智教育","黑马程序员","Python")
index = t6.index("黑马程序员")
print(f"在元组中查找黑马程序员的下标是: {index}")

# 元组的操作: count统计方法
t7 = ("传智教育","黑马程序员","黑马程序员","黑马程序员","Python")
count = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有: {count}")

# 元组的操作: len函数统计元组元素数量
t8 = ("传智教育","黑马程序员","黑马程序员","黑马程序员","Python")
i = len(t8)
print(f"t8中的元素有: {i}个")

# 元组的遍历: while
index = 0
while index < len(t8):
    print(f"元组的元素有: {t8[index]}")
    index += 1

# 元组的遍历: for
for element in t8:
    print(f"元组的元素有: {element}")

# 修改元组的内容
# t8[0] = "itcast"

# 定义一个元组
t9 = (1,2,["itheima","itcast"])
print(f"t9的内容是: {t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是: {t9}")


# 练习
my_tuple = ('周杰伦',11,["football","music"])
# 其年龄所在的下标位置
index = my_tuple.index(11)
print(f"其年龄所在的下标位置是: {index}")
# 查询学生的姓名
index = my_tuple.index("周杰伦")
print(my_tuple[index])
# 删除学生爱好中的football
element = my_tuple[2].pop(0)
print(f"删除学生爱好中的是: {element}")
# 增加爱好
element = my_tuple[2].append("coding")
print(my_tuple)

