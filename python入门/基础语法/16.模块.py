#inport导入模块
import time
print("hello world")
time.sleep(1)  #通过. 使用模块内部的全部功能
print("goodbye world")

# 使用from导入time的sleep功能（函数）
from time import sleep
print("hello world")
sleep(1)   
print("goodbye world")

# 使用 * 导入模块中的全部功能
from time import *   # *表示全部的意思
print("hello world")
sleep(1)   
print("goodbye world")

#使用as给模块取别名
import time as t
print("hello world")
t.sleep(1)   
print("goodbye world")   #使用别名调用模块的功能

#自定义模块
import my_module1
from my_module1 import test
test(114,514)

#导入不同模块的同名功能： 后者覆盖前者

#main变量

#all变量
from my_module2 import *
test_a(1,2)
test_b(3,4)