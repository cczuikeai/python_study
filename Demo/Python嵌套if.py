"""
 if的嵌套使用
 python:
        if 条件1:
            满足条件1做的事1
            满足条件1做的事2
            if 条件2:
                满足条件2做的事1
                满足条件2做的事2
java:
    if (布尔表达式) {
        满足条件1做的事1;
        满足条件1做的事2;
        if (布尔表达式) {
            满足条件2做的事1
            满足条件2做的事2
        }
    }
"""
print("欢迎来到库洛米公园")
if int(input("请输入您的身高: ")) > 120:
    print("您好!您的身高超出限制不能免费游玩!")
    print("但是,如果您的VIP等级大于3的话,可以免费游玩!")

    if int(input("请输入您的VIP等级: ")) > 3:
        print("恭喜您!您的VIP等级达标,可以免费游玩了!")
    else:
        print("Sorry,您的不满足以上两个条件,需要购买10元门票")
else:
    print("欢迎小朋友来游玩")

print("------------公司发礼物------------")
if 30 > int(input("请输入您的年龄: ")) >= 18:
    print("你是成年人,年龄达标了")
    if int(input("请输入您的工龄: ")) > 2:
        print("恭喜您,年龄和工龄都达标了,可以领取礼物")
    elif int(input("请输入您的级别: ")) > 3:
        print("恭喜您,年龄和级别达标了,可以领取礼物")
    else:
        print("不好意思,虽然年龄达标了,但是工龄和级别都不达标,所以不能领取礼物哦")
else:
    print("不好意思,年龄不匹配哦")


print("--------------if的综合练习--------------")
"""
 随机数的概念: random
 Python: 
        import random
        num = random.randint(1,10)
 Java:
        import java.util.Random;
        
        Random r = new Random();
        int i = r.nextInt(10);  //10表示区间
"""

# 1. 构建一个随机数
import random
num = random.randint(1,10)

guess_num = int(input("请输入您要猜测的数字: "))
if guess_num == num:
    print("恭喜您!猜对了")
else:
    if guess_num > num:
        print("猜错了,你猜的数字太大了")
    else:
        print("猜错了,你猜的数字太小了")
    guess_num = int(input("再猜一次,请输入您要猜测的数字: "))
    if guess_num == num:
        print("恭喜您!第二次猜对了")
    else:
        if guess_num > num:
            print("猜错了,你猜的数字太大了")
        else:
            print("猜错了,你猜的数字太小了")



