# 参数 解包 变量
from sys import argv
script, first, second, third = argv
print("result:", script, first, second, int(third))
#the command is: python ex13.py s f t
