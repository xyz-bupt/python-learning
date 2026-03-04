#while循环 嵌套
i = 0  
j = 0
while i < 5:  
    print("快去学习")
    while j < 3:  
        print("今天你敲代码了吗")
        j += 1
    i += 1  
    j = 0

   #for循环
#遍历字符串(无法设置循环条件)
name = "夏北泽先辈114"

for letter in name:
    print(letter) #遍历

#range语句
#range(num) 获取一个从0开始，到num结束的数字序列（不含num本身）
#range(num1,num2) 从num1开始，到num2结束，步长为1的数字序列（不含num本身）
#range(num1,num2,step) 从num1开始，到num2结束，步长为step的数字序列 （不含num本身）
for x in range(114,514,50):
    print(x) 

#作用域
for i in range(5):
    print(i)
print(i)    

#嵌套循环
#循环中断break continue
#continue语句用于跳过当前循环的剩余语句，直接开始下一轮循环。 for循环，while循环 效果一致
#break语句用于终止当前循环，直接跳出循环体。for循环，while循环 效果一致
