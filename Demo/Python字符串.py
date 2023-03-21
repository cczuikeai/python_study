"""
Python中常用的三种占位符
"""

# %s : 将内容转换成字符串,放入占位位置
class_num = 57
avg_salary = 16781
message = "Python大数据学科,北京%s期,毕业平均工资:%s" % (class_num, avg_salary)
print(message)
# %d : 将内容转换成整数,放入占位位置
# %f : 将内容转换成浮点型,放入占位位置,如果写成%.2f就会保留小数点后面两位小数,但是两位后面的小数如果大于5就会四舍五入
# %r ; 将内容转换成浮点数,后面有几位小数就保留几位小数,放入占位位置
name = "传智教育"
setup_year = 2006
stock_price = 19.994
message = "%s,成立于%d,今天的股价是:%.2f" % (name, setup_year, stock_price)
print(message)

"""
字符串格式化-数字精度控制
1. 可以使用"m.n"来控制数据的宽度和精度
    - m,控制宽度,要求是数字(很少使用),设置的宽度小于自身时,不生效
    -.n,控制小数点精度,要求是数字,会进行小数的四舍五入
2. ps:
    - %5d,表示将整数的宽度控制在5位,当数据是11时,就会变成:[空格][空格][空格]11,用三个空格来补足宽度
    - %.2f,表示不限制宽度,只设置小数点精度为2,比如11.345的数据设置为%.2f以后就会变成11.35
"""
num1 = 11
num2 = 11.345
print("数字11宽度限制5,结果是: %5d" % num1)
print("数字11宽度限制1,结果是: %1d" % num1)
print("数字11.345宽度限制7,小数精度2,结果是: %7.2f" % num2)
print("数字11.345宽度不限制,小数精度2,结果是: %.2f" % num2)

"""
 Python字符串格式化的快速写法
 - 语法 : f"内容{变量}"  
 - 这种方式的特点在于它不用理会类型,不做精度控制
 - 适合对精度没有要求时快速使用
"""
name = "传智教育"
setup_year = 2006
stock_price = 19.99
# f: format
print(f"我是{name},我成立于{setup_year},我今天的股价是{stock_price}")

"""
 表达式进行字符串格式化
"""
print("1 * 1 的结果是: %d" % (1 * 1))
print(f"1 * 2 的结果是: {1 * 2}")
print("字符串在Python中的类型名是:%s " % type("字符串"))

name = "传智播客"
stock_code = str("003032")
stock_price = float(19.99)
print(f"公司:{name},股票代码:{stock_code},当前股价:{19.99}")

stock_price_daily_growth_factor = float(1.2)
growth_days = int(7)
finally_stock_price = 19.99*1.2**7
print("每日增长系数是: %r,经过%d天的增长后,股价达到了: %.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))