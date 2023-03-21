"""
 布尔类型与比较运算符
"""
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1的变量内容是: {bool_1},类型是: {type(bool_1)}")
print(f"bool_2的变量内容是: {bool_2},类型是: {type(bool_2)}")

# 比较运算符的使用
# == , != , > , < , >= , <=
num1 = 10
num2 = 10
print(f"10 == 10 的结果是: {10 == 10}")

num1 = 10
num2 = 15
print(f"10 != 15 的结果是: {10 != 15}")


"""
 if判断语句
"""
age = 10
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print('时间过得真快呀')



print("欢迎来到囡囡儿童游乐场,儿童免费,成人收费.")
age = input("请输入您的年龄: ")
age = int(age)
if age >= 18:
    print("您已成年,游玩需要补票10元")
print("祝您游玩愉快!!!")


"""
 if else 语句
"""

print("欢迎来到囡囡儿童游乐场,儿童免费,成人收费.")
age = input("请输入您的年龄: ")
age = int(age)
if age >= 18:
    print("您已成年,游玩需要补票10元")
else:
    print("您未成年,可以免费游玩!")
print("祝您游玩愉快!!!")

print("--------------------------")

print("欢迎来到黑马动物园")
cm = input("请输入您的身高: ")
cm = int(cm)
if cm <= 0 or cm >= 300:
    print("您好,请输入正确的身高!")
elif cm > 120:
    print(f"您的身高超出{120}cm, 游玩需要购票10元")
else:
    print(f"您的身高未超过{120}cm, 可以免费游玩")
print("祝您游玩愉快")



"""
if elif else   语句
"""

print("欢迎来到囡囡动物园!!")
height = int(input("请输入您的身高(cm): "))
print(f"您的身高是: {height}")
vip_level = int(input("请输入您的VIP等级(1-5): "))
print(f"您的VIP等级是: {vip_level}")
day = int(input("请告诉我今天是星期几: "))
print("感谢您提供的信息")
if 120 > height > 0:
    print("您的身高小于120cm,可以免费游玩!")
elif vip_level > 3 and 5 >= vip_level >= 1:
    print("您的VIP等级大于3,可以免费玩!")
elif day == 1:
    print("今天是1号免费日哦,可以免费游玩")
else:
    print("不好意思,条件都不满足,组要买票10元!")
print("祝您玩的开心!!")

print("--------------------------------")

if int(input("请输入您的身高(cm) : ")) < 120:
    print("您的身高小于120,可以免费游玩")
elif int(input("请输入您的VIP等级 (1-5) : ")) > 3:
    print("您的VIP等级大于3,可以免费游玩")
elif int(input("请告诉我今天是星期几: ")) == 1:
    print("今天是1号免费日哦,可以免费游玩")
else:
    print("不好意思,条件都不满足,需要买票10元")

print("----------------练习----------------")
print("让我们来玩猜数字游戏吧!")
num = 50
if int(input("请输入第一次猜想的数字: ")) == num:
    print("恭喜你,猜对了!")
elif int(input("不对,再猜一次: ")) == num:
    print("恭喜你猜对了!")
elif int(input("不对,再猜最后一次: ")) == num:
    print("恭喜你,猜对了!")
else:
    print(f"Sorry,全部猜错了,我想要的是: {num}")

