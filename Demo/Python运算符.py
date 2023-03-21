"""
演示Python中的各种运算符
"""

# 算术(数学)运算符
print("1+1=",1+1)
print("5-3=",5-3)
print("5*3=",5*3)
print("9/3=",9/3)
print("5//3=",5//3)
print("5%3=",5%3)
print("5**3=",5**3)
# 赋值运算符
# +=,-=
num = 1
num += 1
print("num+=1:",num)
num -= 1
print("num-=1:",num)
num *= 4
print("num*=4:",num)
num /= 2
print("num/=2:",num )
num = 3
num %=2
print("num%=2:",num)
num **= 2
print("num**=2:",num)
num = 8
num //= 2
print("num//=2:",num)

print(type(input("请输入您的结果: ")))
