#多返回值
def test_return():
    return 1, 'hello', True

a, b, c = test_return()
print(a, b, c)

#函数多种传参方式 :位置；关键字；缺省；不定长
def user_info(name,age,gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")

#位置参数
user_info('张三',20,'男')
#关键字参数
user_info(age=20,gender='女',name='张三')
user_info(gender='男',name='李四',age=25)  #可以不按照参数的定义顺序传参
user_info('田所浩二',gender='先辈',age=24)
#缺省参数 (提供默认值)
def user_info(name,age,gender = '男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")

user_info('张三',20)

   #不定长参数
#1.位置传递  *号
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")


user_info('张三',20,'男')
user_info('田所浩二',24,'先辈','南通')


#2.关键字传递 **号
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是：{kwargs}")

user_info(name='张三',age=20,gender='男')
user_info(name='田所浩二',age=24,gender='先辈',city='南通')



#函数作为参数传递
def test_func(compute):
    result = compute(10,20)
    print(f"计算结果是：{result}")
    print(f"计算函数的类型是：{type(compute)}")

def compute(a,b):
    return a+b

test_func(compute)

#lambda匿名函数  一次性使用
def test_func(compute):
    result = compute(114,514)
    print(f"计算结果是：{result}")
    print(f"计算函数的类型是：{type(compute)}")

test_func(lambda a,b:a+b)
