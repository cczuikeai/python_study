"""
综合案例：黑马ATM
定义一个全局变量：money，用来记录银行卡余额（默认5000000）
定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
定义如下的函数：
查询余额函数
存款函数
取款函数
主菜单函数
要求：
程序启动后要求输入客户姓名
查询余额、存款、取款后都会返回主菜单
存款、取款后，都应显示一下当前余额
客户选择退出或输入错误，程序会退出，否则一直运行
"""
# 定义全局变量money,name
money = 5000000
name = None
# 要求客户输入姓名
name = input("请输入您的姓名: ")


# 定义查询函数
def query(show_header):
    if show_header:
        print("------------查询余额------------")
    print(f"{name},您好,您的余额剩余: {money}元")


# 定义存款函数
def saving(num):
    global money  # 将money在函数内部定义为全局变量
    money += num
    print("------------存款------------")
    print(f"{name},您好,您存款{num}成功")

    # 调用查询余额的函数
    query(False)


# 定义取款函数
def get_money(num):
    global money  # 将money在函数内部定义为全局变量
    money -= num
    print("------------取款------------")
    print(f"{name},你好,您取款{num}成功")

    # 调用查询余额的函数
    query(False)


# 定义主菜单函数
def main():
    print("------------主菜单------------")
    print(f"{name},您好,欢迎来到晨晨银行ATM,请选择操作:")
    print("查询余额\t[1]")
    print("存款\t\t[2]")
    print("取款\t\t[3]")
    print("退出\t\t[4]")
    return input("请输入您的选择: ")  # 直接返回输入的结果,这边输入的是一个str类型


# 设置无限循环,确保程序不退出
while True:
    keyboard_input = main()  # 用一个变量去接收main函数,main函数是用来显示主菜单页面的
    # 判断输入的数字是几,并对其做格式转换,转成int类型
    if keyboard_input == "1":
        query(True)  # 通过continue继续下一次循环,一进来就回到了主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存入多少钱?请输入: "))  # 这边进行了int类型的格式转换,把输入的值转换成了具体的数字
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱?请输入: "))
        get_money(num)
        continue
    else: 
        print("程序退出了")
        break  # 通过break退出循环
