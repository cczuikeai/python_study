"""
 input语句(函数)
 - 和java中的scanner差不多,键盘输入
 - 获取的永远是字符串类型的数据,如果要输入整数类型就要先转类型
"""
# print("请告诉我你是谁?")
name = input("请告诉我你是谁? ")
print("Get!!!! 你是: %s" % name)

num = input("请告诉我你的银行卡密码: ")
num = int(num)
print("你的银行卡密码的类型是: ",type(num))
print(f"我的密码是{num}")

user_name = input("请告诉我您的用户名是什么? ")
print(f"我的用户名是: {user_name}")
user_type = input("请告诉我您的用户类型是什么? ")
print(f"我的用户类型是: {user_type}")
print("好的,谢谢您提供的信息!")
print("您好: %s, 您是尊贵的: %s用户,欢迎您的光临!!" % (user_name,user_type))
