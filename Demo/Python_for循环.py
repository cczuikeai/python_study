"""
for循环
    Python:
            for 临时变量 in 待处理数据集:
                循环满足条件时执行的代码
    Java:   for (条件表达式1(循环的初始部分,赋值语句),条件表达式2(循环条件,条件语句),条件表达式3(运算符循环结构的迭代部分,迭代语句))
            {
                语句块
            }

    - 作用域 for循环中的临时变量在编程规范上,作用域只在for循环内部
    - 在外部访问实际上是可以访问的,但是规范上是不允许的
"""

name = "cczuikeai"

for x in name:
    # 将name的内容,逐个取出赋予x临时变量
    # 这样就可以在循环体内对x进行处理了
    print(x)


# 统计字符含有几个a
name = "itheima is a brand of itcast"

# 定义一个变量,来统计有多少个a
count = 0

# for循环统计
# for 临时变量 in 被统计的数据
for x in name:
    if x == "a":
        count += 1
print(f"{name}中包含有: {count}个字母a")

"""
嵌套for
"""
i = 1
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天,加油坚持.")
    # 写内层循环
    for j in range(1,11):
        print(f"给小美送的第{j}朵玫瑰花")
    print("小美我喜欢你")
print(f"第{i}天,表白成功")


i = 1
for i in range(1,10):
    j = 1
    for j in range(1,i+1):
        print(f"{j} * {i} = {j * i}\t",end="")
