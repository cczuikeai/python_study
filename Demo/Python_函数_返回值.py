"""
    函数返回值
"""
# 定义一个函数,实现两数相加
def add(x,y):
    """
    add函数可以接受2个参数,进行2数相加的功能
    :param x: 形参x表示相加的一个数字
    :param y: 形参y表示想家的另一个数字
    :return: 返回值是两数相加的结果
    """
    result = x+y
    return result
result = add(5,6)
print(f"结果为: {result}")

# 无result语句的函数返回值
def say_hi():
    print("你好呀")
result1 = say_hi()
print(f"无返回值函数,返回的内容是{result1}")
print(f"无返回值函数,返回的内容类型是{type(result1)}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result2 = check_age(20)
if not result2:
    # 进入if表示result2是None值,也就是False
    print("未成年,不得入内")
