"""
- Python中的字典,是以key - value的形式出现的
  相当于Java中的键值对
- 字典的定义,同样使用{},但是里面存放的是一个个的键值对
- 定义字面量
{key: value, key: value,key: value...}
- 定义字面量变量
my_dict = {key: value, key: value,key: value...}
- 定义空字典
my_dict = {}
my_dict = dict()

字典和集合一样不可以使用下标索引
"""
# 定义字典
my_dict = {"王力宏": 99, "周杰伦": 88, "凌俊杰": 77}

# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是: {my_dict},类型是: {type(my_dict)}")
print(f"字典2的内容是: {my_dict2},类型是: {type(my_dict2)}")
print(f"字典3的内容是: {my_dict3},类型是: {type(my_dict3)}")

# 定义重复key的字典
my_dict1 = {"王力宏": 99, "王力宏": 88, "凌俊杰": 77}
print(f"重复key的字典的内容是: {my_dict1}")

# 从字典中基于key获取value
my_dict1 = {"王力宏": 99, "周杰伦": 88, "凌俊杰": 77}
score = my_dict1["周杰伦"]
print(f"周杰伦的考试分数为: {score}")

# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "周杰伦": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是: {stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下周杰伦的语文信息
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文分数是: {score}")


"""
字典的常用操作
"""
my_dict = {"周杰伦": 99, "林俊杰": 88,"张学友": 77}

# 新增元素
# 语法: 字典["key"] = value     这边是key不存在
my_dict["张信哲"] = 66
print(f"字典经过新增元素后,结果: {my_dict}")

# 更新操作
# 语法: 字典["key"] = value     这边是key存在
my_dict["周杰伦"] = 33
print(f"字典经过更新元素后,结果: {my_dict}")

# 删除操作
# 语法: 字典.pop(key)
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素,结果: {my_dict}, 周杰伦的考试分数是: {score}")

# 清空元素
# 字典.clear()
my_dict.clear()
print(f"字典被清空了, 内容是: {my_dict}")

# 获取全部的key
my_dict = {"周杰伦": 99, "林俊杰": 88,"张学友": 77}
keys = my_dict.keys()
print(f"字典中的全部keys是: {keys}")

# 遍历字典
# 方式一: 通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的全部key是: {key}")
    print(f"字典的全部value是: {my_dict[key]}")

# 方式二: 直接对字典进行for循环,每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的全部key是: {key}")
    print(f"字典的全部value是: {my_dict[key]}")

# 统计字典内的元素数量        len(字典)
count = len(my_dict)
print(f"字典中的元素数量有: {count}")


print("---------------------------")
# 练习
my_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },"周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },"林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },"张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },"刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(f"全体员工当前信息如下: {my_dict}")
for key in my_dict:
    if my_dict[key]["级别"] == 1:
        my_dict[key]["级别"] += 1
        my_dict[key]["工资"] += 1000
print(f"全体员工级别为1的员工完成升职加薪操作,操作后: \n{my_dict}")
