#定义
def say_hi():
    print("hi")

#调用
say_hi()

#传入 返回值
def add(x, y):
    return x + y
result = add(2, 3)
print(result)

#None
a = say_hi()
print(f"无返回值函数，返回的内容是：{a}")
print(f"无返回值函数，返回的内容类型是：{type(a)}")
