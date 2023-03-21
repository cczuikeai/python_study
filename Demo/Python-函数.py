"""
函数的开发和使用
    Python: def 函数名(传入参数):
                函数体
                return返回值
                变量 = 函数(参数)
    Java:   [修饰符] 返回值类型 方法名称 ([参数表]){
            方法体 //具体的功能
            (返回值)
    }

    函数定义中的参数是形式参数
    函数调用中的参数是实际参数
"""

# str1 = "itheima"
# str2 = "itcast"
# str3 = "python"
#
# # 定义一个计数的变量
# count = 0
# for i in str1:
#     count +=1
# print(f"字符串{str1}的长度是: {count}")

# 定义一个函数,输出相关信息
from Python_for循环 import x


def say_hi():
    print("Hi,你好呀,傻逼")
# 调用函数,让定义的函数工作
say_hi()

def auto():
    print("欢迎来到库洛米晨堡! \n请出示您的健康码,以及72小时核酸证明")

auto()

def add(x,y):
    result = x + y
    print(f"{x}+{y}的计算结果为: {result}")
add(4,5)

def temperature(x):
    x = float(x)
    print("欢迎来到黑马程序员!请出示您的健康码以及72小时核酸证明,并配合测量体温!")
    if x <= 37.5:
        print(f"测量体温中,您的体温是: {x}度,体温正常请进!")
    else:
        print(f"测量体温中,您的体温是: {x}度,需要隔离!")

for x in range(5):
    x = float(input("请输入您的体温: "))
    temperature(x)


def func_b():
    print("---2---")
def func_a():
    print("---1---")
    # 嵌套使用func_b
    func_b()
    print("---3---")
# 调用func_a
func_a()