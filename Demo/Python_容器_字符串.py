"""
容器中的字符串

特点:
    - 只可以储存字符串
    - 长度任意(取决于内存大小)
    - 支持下标索引
    - 允许重复字符串存在
    - 不可以修改(增加或删除等)
    - 支持for循环

字符串不可修改
"""
my_str = "itheima  and itcast"

# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}去下标为2的元素,值是: {value},取下标为-16的元素,值是: {value2}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and,其起始下标是: {value}")

# replace方法     替换,是在原来的基础上创造出一个新的字符串,并不是原来的字符串,原来的字符串是不能被修改的
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str},进行替换后得到: {new_my_str}")

# split方法       切割
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到: {my_str_list}, 类型是: {type(my_str_list)}")

# strip方法   整归操作,去除年后空格
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()  # 不传入参数,去除收尾空格
print(f"字符串{my_str}被strip后,结果是: {new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后,结果是: {new_my_str}")

# 统计字符串中某字符串的出现次数
my_str = "itheima and itcast"
new_my_str = my_str.count("i")
print(f"字符串{my_str}被count后,i出现的次数为: {new_my_str}")

# 统计字符串的长度
my_str = "itheima and itcast"
new_my_str = len(my_str)
print(f"字符串{my_str}的字符串总长度为: {new_my_str}")

my_str = "库洛米公主大人"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

for i in my_str:
    print(i)

# 练习
# 统计字符串it有几个       对象.count
my_str = "itheima itcast boxuegu"
new_my_str = my_str.count("it")
print(f"字符串{my_str}中含有{new_my_str}个it")

# 将空格替换成"|"     对象.replace
my_str = "itheima itcast boxuegu"
new_my_str = my_str.replace(" ","|")
print(f"字符串{my_str}用replace后,结果是: {new_my_str}")

# 按照"|"分割,得到列表      对象.split
new_my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}被split分割后的到的列表为: {new_my_str_list}")



