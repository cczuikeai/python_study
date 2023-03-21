"""
变量的作用域
    - 局部变量
        - 定义在函数体内部的变量,只在函数体内部生效
        - 作用在函数体内部,临时保存数据,当函数调用完的时候,局部变量就会被销毁
    - 全局变量
        - 在函数体内,体外都能生效的变量

    global关键字相当于Java的this关键字,把局部变量变成全局变量
"""
# 局部变量
def test_a():
    num = 100
    print(num)
test_a()
# 出了函数体,局部变量就没办法使用
# print(num)

# 全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
# def test_b():
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
# def test_b():
#     num = 500
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# global关键字,在函数内声明变量为全局变量
num = 200

def test_a():
    print(f"test_a: {num}")
def test_b():
    global num  # 设置内部定义的变量为全局变量相当于Java的this
    num = 500
    print(f"test_b: {num}")

test_a()
test_b()
print(num)