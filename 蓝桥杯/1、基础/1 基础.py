s = '123456789'

print(s)   #输出字符串
print(s[0:-1])   #输出第一个到倒数第二个的所有字符
print(s[2:5])   #输出从第三个开始到第五个的字符
print(s[2:])   #输出从第三个开始后的所有字符
print(s[1:5:2])   #输出从第二个开始到第五个且步长为2
print(s * 2)   #输出字符串两次
print(s + 'abc')   #输出字符串和'abc'连接


#自定义分隔符
#使用 'sep' 参数指定分隔符
print(1,2,3,4,5, sep='-')   #输出1-2-3-4-5

#自定义结束符
#使用 'end' 参数指定结束符 （默认为换行符'\n'）
print(1,2,3,4,5, end='-')   #输出12345-


print('\n')


#格式化输出
# - 使用 'f-string'
# 格式： print(f'{variable}')
name = 'Alice' ; print(f'Hello, {name}!')   #输出Hello, Alice!
# - 使用 'format' 方法
# 格式： print('{}'.format(variable))
age = 25 ; print('My age is {}.'.format(age))   #输出My age is 25.


#高效输出
#使用 print(*list) 快速输出列表内容
lst = [1,2,3];  print(*lst)

#数据类型： 整数 浮点数 字符串 列表 元组 集合 字典

"""可变参数
可变参数是python函数中一种灵活的参数传递方式，允许函数接收任意数量的参数，分两种形式：
*args : 用于接收任意数量的位置参数，并将其打包成一个元组
**kwargs : 用于接收任意数量的关键字参数，并将其打包成一个字典
"""

#可变参数
def my_sum(*args):
    return sum(args)
print(my_sum(1,2,3,4,5))   #输出15

#关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Alice', age=30, city='New York')



