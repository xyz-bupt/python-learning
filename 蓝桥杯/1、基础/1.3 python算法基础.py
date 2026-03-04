#快读模板
import sys
input = lambda:sys.stdin.readline().strip()

#lambda表达式
"""
基本语法：
lambda 参数:表达式
"""
x = lambda a: a+10
print(x(5)) # 15   
"""
这里，lambda是python的关键字，用于定义lambda函数。参数是参数列表，可以包含零个活多个参数，但必须在冒号（：）前指定
表达式是一个用于计算并返回函数结果的表达式
例如，创建一个lambda函数，它接受一个参数并返回该参数加10的结果：
"""
#获得中位数
get_mid = lambda nums:nums[len(nums) // 2]
print(get_mid([1, 2, 3, 4, 5])) # 3


#内置排序算法
"""
sorted()函数
python内置的sorted()函数可以对任何可迭代对象进行排序，返回一个新的排序后的列表
基本语法：
sorted(iterable, key=None, reverse=False)
iterable: 需要排序的可迭代对象
key: 排序规则，可以传入一个函数，指定排序依据(如按元素的某个属性排序)
reverse: 是否反向排序，默认为False,表示升序排序
"""
#按照默认升序排序
nums = [5, 3, 8, 6, 7]
print(sorted(nums)) # [3, 5, 6, 7, 8]
#按照降序排序
print(sorted(nums, reverse=True)) # [8, 7, 6, 5, 3]
#按照字符串长度排序
words = ['apple', 'banana', 'orange', 'pear']
print(sorted(words, key=len)) # ['pear', 'apple', 'banana', 'orange']


#输入
#处理常见输入格式
#1.单行多个整数
a,b,c = map(int, input().split())  #假设输入：1 2 3
print(a,b,c) # 1 2 3
#2.多行多个整数
n = int(input()) # 输入行数
lst = []
for _ in range(n):
    lst.extend(map(int, input().split())) # 每行输入多个整数
print(lst) # 输出所有整数的列表
#3.矩阵输入
n, m = map(int,input().split()) # 输入矩阵行列数
matrix = [list(map(int, input().split())) for _ in range(n)] # 输入n行m列矩阵
print(matrix)