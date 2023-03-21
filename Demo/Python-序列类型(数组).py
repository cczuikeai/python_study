"""
range语句
    - 数字序列
    - 相当于Java的数组
    - 三种语法
        - range(num): 获取从0开始,到num结束的数字序列,不包含num本身       ps: range(5)    [0,1,2,3,4]
        - range(num1,num2): 获取从num1开始,到num2结束的数字序列,不包含num2本身,和Java说的含头不含尾一样     ps: range(5,10)     [5,6,7,8,9]
        - range(num1,num2,step): 和第二种差不多,多了一个step,数字之间的步长,以step为准,默认是1      ps:range(5,10,2)       [5,7,9]
"""

# range语法一: range(num)
for x in range(10):
    print(x)

# range语法二: range(num1,num2)
for x in range(5,10):
    # 从5开始,到10结束,但是不包含10本身
    print(x)

# range语法三: range(num1,num2,step)
for x in range(5,10,2):
    # 从5开始,到10结束,但是不包含自己,数字之间的间隔是2
    print(x)


for x in range(10):
    print("送了一个超级火箭")


print("-----------练习-----------")
count = 0
for x in range(1,100):
    if x%2 == 0:
        count += 1
#        print(x)
print(f"1到100(不包含100本身)范围内,有{count}个偶数")
