"""
序列的概念:
    - 内容连续,有序,可使用下标索引的一类数据容器
    - 列表,元组,字符串都是序列
序列的切片操作:
    - 切片就是从一个序列中,取出一个子序列
序列的语法:
    - 序列[起始下标:结束下标:步长]      表示从序列中,从指定位置开始,一次取出元素,到指定位置结束,得到一个新序列
    - 起始位置表示从何处开始,可以留空,留空视做从头开始
    - 结束下标(不含)表示何处结束,可以留空,留空视作截取到结尾
    - 步长表示依次取元素的间隔
        - 步长N表示,每次跳过N-1个元素
        - 步长负数是表示,反向取
对序列进行切片,不会影响序列本身,而是会创造出一个新的序列
"""
# 对list进行切片,从1开始,4结束,步长1
my_list = [0,1,2,3,4,5,6,]
result1 = my_list[1:4]       # 步长默认是1,可以省略不写
print(f"结果是1: {result1}")

# 对tuple 进行切片,从头开始,到最后结束,步长1
my_tuple = [0,1,2,3,4,5,6,]
result2 = my_tuple[:]       # 起始和结束不写表示从头到尾,步长1可以省略
print(f"结果2是: {result2}")

# 对str进行切片,从头到尾,步长2
my_str = "0123456"
result3 = my_str[::2]
print(f"结果3是: {result3}")

# 对str字符串进行切片,从头到尾,步长-1
my_str = "0123456"
result4 = my_str[::-1]
print(f"结果4是: {result4}")

# 对列表进行切片,从3开始,到1结尾,步长-1
my_list = [0,1,2,3,4,5,6,]
result5 = my_list[3:1:-1]
print(f"结果5是: {result5}")

# 对元组进行切片,从头到尾,步长-2
my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::-2]
print(f"结果6为: {result6}")

# 练习
# 先用split方法,把字符串str1以","分割成列表
# 然后再去定位"员序程马黑来"的下标
# 找到下标以后,运用对列表的反向切片原理,把"员序程马黑来"转换成"来黑马程序员"
# 这时候我们得到一串新的字符串,再去用字符串的api方法".replace"来将"来"替换成""
# 输出
str1 = "万过薪月,员序程马黑来,nohtyP学"
print(str1.split(",")[1][::-1].replace("来",""))
