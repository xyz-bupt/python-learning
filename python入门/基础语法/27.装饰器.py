#装饰器其实也是一种闭包，其功能是在不破坏函数原有的代码和功能的前提下，为目标函数增加新功能

#装饰器的一般写法（闭包写法）
# def outer(func):
#     def inner():                       #定义一个闭包函数，在闭包函数内部：执行目标函数；并完成功能的添加
#         print("我要睡觉了")
#         func()
#         print("我起床了")

#     return inner

# def sleep():                         #通过闭包函数为sleep增加功能
#     import random
#     import time
#     print("睡眠中。。。。。。")
#     time.sleep(random.randint(1,5))

# fn = outer(sleep)                    #相当于把sleep函数转为inner函数用
# fn()


#装饰器的快捷写法（语法糖）
def outer(func):
    def inner():                       
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():                         
    import random
    import time
    print("睡眠中。。。。。。")
    time.sleep(random.randint(1,5))

sleep()
