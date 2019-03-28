# exercise6 字符串和文本
x = "There are %d types of people"%10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s."%(binary,do_not)
print(x)
print(y)
#布尔型 敏感大小写False 用 false不可
hilarious=False
joke_evaluation = "Isn't that joke so funny %r?"
print(joke_evaluation%hilarious)
# %r 打印会加单引号，显示的是变量“原始”的数据值 ；%s %d %f 等是格式化字符串后，确定了字符串的值类型