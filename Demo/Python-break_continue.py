"""
    - continue: 中断本次循环,直接进入下一循环             临时中断
        - 应用场景: 在循环中,因为某些原因要临时结束本次循环
    - break: 直接结束循环        永久中断
作用域: 本次循环内,对上层循环无效

"""
# continue的应用
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")

# continue的嵌套应用
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# break中断语句
for i in range(1,101):
    print("语句1")
    break
    print("语句2")
print("语句3")

# break的嵌套语句
for i in range(1,101):
    print("语句1")
    for j in range(1,101):
        print("语句2")
        break
        print("语句3")
    print("语句4")


print("----------综合案例-发工资----------")
"""
某公司，账户余额有1W元，给20名员工发工资。
员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
领工资时，财务判断员工的绩效分（1-10）随机生成，如果低于5，不发工资，换下一位
如果工资发完了，结束发工资。
"""
"""
先定义账户余额
money = 10000
import random

员工编号: range(1,21)
"""
# 先定义账户余额
money = 10000
# for循环对员工进行发工资
for i in range(1,21):
    # 先要对其判断他的绩效分
    # 随机生成的绩效分用random
    import random
    score = random.randint(1,10)
    # 判断绩效分,if语句,低于5分下一位用score < 5和 continue来写
    if score < 5:
        print(f"员工{i},绩效分{score},低于5分,不发工资,下一位")
        # 通过continue跳过发放
        continue
    # 判断公司余额足不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i},满足条件发放工资1000,公司账户余额: {money}元")
    else:
        print(f"余额不足,当前余额: {money}元,不足以发工资,不发了,下个月再来")
        # 通过break结束整个循环
        break

