'''
#列表推导器
"""
[expression for item in iterable if condition]
- expression: 表达式，用于生成列表中的元素
- item: 可迭代对象中的每个元素
- iterable: 可迭代对象，如列表、字符串,range等
- condition: 可选，用于过滤元素的条件
"""

#示例1: 生成1到10的平方数列表
squares = [i**2 for i in range(1,11)]
print(squares)   #输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#示例2: 生成1到10的偶数列表
evens = [i for i in range(1,11) if i%2 == 0]
print(evens)   #输出: [2, 4, 6, 8, 10]

#示例3: 将输入的字符串列表转换为整数列表
#假设输入为“1 2 3 4 5”
input_data = list(map(int, input().split()))
print(input_data)
#列表推导器实现
input_data = [int(x) for x in input().split()]
print(input_data)
#输出： [1, 2, 3, 4, 5]

#示例4: 生成一个nxn的零矩阵
n = 3
#zero_matrix = [[0 for _ in range(n)] for _ in range(n)]
zero_matrix = [[0 for j in range(n)] for i in range(n)]
print(zero_matrix)
# 输出: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#示例5: 快速生成一个长度为n的斐波那契数列  f(n)
n = 10
fib = [0, 1]
#[fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
[fib.append(fib[-1] + fib[-2]) for i in range(n-2)]
print(fib)

#示例6: 将二维列表展平为一维列表
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)   #输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#示例7: 快速统计字符串中每个字符的出现次数
s = "algorithm"
char_count = {char: s.count(char) for char in set(s)}
print(char_count)   #输出: {'a': 1, 'l': 3, 'g': 2, 'o': 2, 'r': 1, 'i': 1, 't': 1}
'''


'''
#range函数
"""
range(start, stop, step)
-start: 序列的起始值(包含), 默认为0
-stop: 序列的结束值（不包含
-step: 步长, 默认为1

range返回的是一个range对象，它是一个惰性序列，节省内存。
如果需要列表，可以用list()函数将其转换为列表
"""

#示例1: 生成0到9的序列(基础用法)
seq = range(10)
print(list(seq))   #输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#示例2: 生成1到10的奇数序列(步长控制)
seq = range(1, 11, 2)
print(list(seq))   #输出: [1, 3, 5, 7, 9]

#示例3: 生产倒序序列(步长为负数)
seq = range(10, 0, -1)
print(list(seq))   #输出: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]   

#示例4: 生成循环的索引(模运算结合)
n = 5
for i in range(n * 2):
    idx = i % n  #索引循环 0-1-2-3-4-0-1-2...
    print(idx, end=' ')   #输出: 0 1 2 3 4 0 1 2 3 4

#示例5: 生成二维网格坐标(嵌套循环)
rows, cols = 2,3
grid = [(i, j) for i in range(rows) for j in range(cols)]
print(grid)  # 输出：[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

#示例8：生成螺旋矩阵(复杂索引控制)
n = 3
matrix = [[0] * n for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
x, y, num, d = 0, 0, 1, 0
for step in range(n, 0, -2):
    for _ in range(4 if step > 1 else 1):
        dx, dy = directions[d]
        for _ in range(step - 1):
            matrix[x][y] = num
            num += 1
            x += dx
            y += dy
        d = (d + 1) % 4
if n % 2 == 1:
    matrix[n//2][n//2] = num
print(matrix)   #输出: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
'''


#双端队列
"""
竞赛应用场景：
- 队列：BFS层序遍历、滑动窗口 等
- 栈：DFS路径回溯、括号匹配、单调栈优化
"""
#栈：只允许从一端插入和删除的线性表
#队列：只允许从一端插入、另一端删除的线性表
#双端队列：允许从两端插入、两端删除的线性表

#队列：先进先出
"""
from collections import deque

q = deque()   # 初始化
q.append(x)   # 从右侧入队
# q.appendleft(x)   # 从左侧入队 （特殊场景用）
x = q.popleft()   # 从左侧出队 (时间复杂度O(1))
len(q)   # 队列长度
"""

#栈：先进后出
"""
stk = []   # 使用列表模拟
stk.append(x)   # 入栈
x = stk.pop()   # 出栈(默认弹出最后一个元素, O(1时间复杂度))
stk[-1]   # 获取栈顶元素不移除
"""

"""
在 Python 列表 stk 中，stk[数字] 表示访问栈（列表）中不同位置的元素：

stk[0]：第一个元素（栈底元素）
stk[1]：第二个元素
stk[2]：第三个元素
...
stk[-1]：最后一个元素（栈顶元素，通常是最新入栈的）
stk[-2]：倒数第二个元素
stk[-3]：倒数第三个元素
...
例子：
stk = [10, 20, 30, 40]
print(stk[0])   # 输出 10，栈底
print(stk[1])   # 输出 20
print(stk[-1])  # 输出 40，栈顶
print(stk[-2])  # 输出 30

总结：
正数索引从左往右（0是第一个）
负数索引从右往左（-1是最后一个，-2是倒数第二个）
"""

#实用技巧：
"""
- 快速判断空队列/栈：if not q:   #判空
- 栈的翻转: stack[::-1]   #用切片获取逆序
"""

# 输入: 10 20 30 40 50
nums = list(map(int, input().split()))
nums_with_index = list(enumerate(nums))  # 从0开始编号
print(nums_with_index)
# 输出: [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]

# 从1开始编号
nums_with_index = [(i+1, num) for i, num in enumerate(nums)]
print(nums_with_index)
# 输出: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]