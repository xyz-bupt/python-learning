#bool类型
result = 10>5
print(result) #True
print (type(result)) #bool
print(int (result))  #1

#if else 判断
age = int(input("请输入你的年龄"))
if age >=18:
    print(f"今年你{age}岁")
    print("你可以去网吧玩")
else:
    print(f"你{age}岁还小，不能去网吧玩")

#if elif else 多条件判断
#判断语句嵌套


#例题
import random
num = random.randint(1,10)
num1 = int(input("请猜测一个1-10之间的数字："))
if num1 == num:
    print("恭喜你猜对了！")
else:
    if num1 > num:
        print("猜大了！")
    else:
        print("猜小了！")

    num1 = int(input("请再次输入你猜测的1-10之间的数字："))    

    if num1 == num:
        print("恭喜你猜对了！")
    else:
        if num1 > num:
            print("猜大了！")
        else:
            print("猜小了！")

        num1 = int(input("请再次输入你猜测的1-10之间的数字："))    

        if num1 == num:
            print("恭喜你猜对了！")
        else:
            print(f"三次机会用完了，抱歉！正确答案是{num}")
    
    