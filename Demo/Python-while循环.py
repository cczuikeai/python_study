"""
 while循环语句
 Python:
        while 条件:
            条件满足时,做的事情1
            条件满足时,做的事情2
            条件满足时,做的事情3
            条件满足时,做的事情4
                ......等待
 Java:
        while (条件)
        {
            条件满足时,做的事1;
            条件满足时,做的事2;
            条件满足时,做的事3;
        }

"""

# i = 0
# while i < 100:
#     print("晨晨我喜欢你")
#     i += 1

# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i += 1
# print(f"1-100的总和为: {sum}")

# import random
# num = random.randint(1, 100)
# count = 0
# # flag = True
# while True:
#     guess_num = int(input("猜一猜数字是几: "))
#     count += 1
#     if num == guess_num:
#         print("猜对了")
#         break
#     if guess_num > num:  print("您猜的数字大了")
#     else:  print("你猜的数字小了")
# #    flag = False
# print(f"您一共猜了: {count}次")


# import random
# #设置随机数生成范围（min——max）
# number_min=int(input("输入想猜测数的最小值:"))
# number_max=int(input("输入想猜测数的最大值:"))
# freedom=random.randint(number_min,number_max)
# num=int(input("输入你猜测的数字："))
# #猜测次数统计
# totle=1
# #条件判断及循环
# while(num!=freedom):
#     if (num > freedom):
#         num = int(input("你猜大了\n请继续输入："))
#         totle+=1
#     elif(num< freedom):
#         num = int(input("你猜小了\n请继续输入："))
#         totle+=1
#     if(num!=freedom and totle==3):
#         print("已猜三次,未猜中，YOU LOST！！！")
#         break
# if (num == freedom):
#     print("恭喜你猜对了")


"""
 while 循环嵌套
"""
# 外层: 表白100天的控制
# 内层: 每天的表白都送10朵玫瑰花的控制
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天,准备表白了.....")
#     j = 1
#     while j<=10:
#         print(f"送给小美第{j}束玫瑰花")
#         j += 1
#     print("小美,我喜欢你")
#     i +=1
# print(f"坚持到第{i-1}天,表白成功")

"""
99乘法表
    - "\t"表示制表符,让多行字符串对齐 
    - end =' '表示让print不换行
"""
# 定义外层循环的控制变量   外层控制行的循环
i = 1
while i <= 9:
    # 定义内层循环的控制变量   内层控制每一行输出的内容
    j = 1
    while j <= i:
        print(f"{j}*{i} = {j*i}\t", end=' ')
        j += 1
    i += 1
    print()
