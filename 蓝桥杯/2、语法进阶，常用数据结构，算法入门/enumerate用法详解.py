"""
========================================
enumerate 函数详解 - 自动编号迭代器
========================================

enumerate() 是Python内置函数，用于在遍历时同时获取索引和元素值。

基本语法：
    enumerate(iterable, start=0)

参数：
    - iterable: 可迭代对象（列表、字符串、元组等）
    - start: 起始编号，默认为0

返回值：
    - 返回一个枚举对象，产生 (索引, 元素) 元组
"""

# ========================================
# 一、基础用法
# ========================================

print("=" * 50)
print("一、基础用法")
print("=" * 50)

# 示例1：遍历列表获取索引和值
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")
# 输出:
# 索引 0: apple
# 索引 1: banana
# 索引 2: cherry

print()

# 示例2：从1开始编号
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果: {fruit}")
# 输出:
# 第1个水果: apple
# 第2个水果: banana
# 第3个水果: cherry

print()


# ========================================
# 二、创建带编号的列表
# ========================================

print("=" * 50)
print("二、创建带编号的列表")
print("=" * 50)

# 示例3：转换为编号列表
nums = [10, 20, 30, 40, 50]
indexed_nums = list(enumerate(nums))
print(f"从0开始: {indexed_nums}")
# 输出: [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]

# 从1开始编号
indexed_nums_from1 = list(enumerate(nums, start=1))
print(f"从1开始: {indexed_nums_from1}")
# 输出: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

print()


# ========================================
# 三、列表推导式组合使用
# ========================================

print("=" * 50)
print("三、列表推导式组合使用")
print("=" * 50)

# 示例4：调整格式 - 编号在前，值在后
nums = [10, 20, 30]
result1 = [(i, num) for i, num in enumerate(nums)]
print(f"编号在前: {result1}")
# 输出: [(0, 10), (1, 20), (2, 30)]

# 示例5：调整格式 - 值在前，编号在后
result2 = [(num, i) for i, num in enumerate(nums)]
print(f"值在前: {result2}")
# 输出: [(10, 0), (20, 1), (30, 2)]

# 示例6：从1开始编号，值在前
result3 = [(num, i+1) for i, num in enumerate(nums)]
print(f"值在前(编号从1): {result3}")
# 输出: [(10, 1), (20, 2), (30, 3)]

print()


# ========================================
# 四、输入场景应用
# ========================================

print("=" * 50)
print("四、输入场景应用")
print("=" * 50)

# 模拟输入（实际使用时去掉这行，使用下面的 input()）
# input_data = "10 20 30 40 50"
# nums = list(map(int, input_data.split()))

# 示例7：一行输入，自动编号
print("方式A：使用 enumerate 直接转换")
nums = [10, 20, 30, 40, 50]  # 实际: nums = list(map(int, input().split()))
indexed = list(enumerate(nums, start=1))
print(f"结果: {indexed}")
# 输出: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

print()
print("方式B：使用列表推导式自定义格式")
indexed_custom = [[i+1, val] for i, val in enumerate(nums)]
print(f"结果(列表形式): {indexed_custom}")
# 输出: [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]

indexed_custom2 = [[val, i+1] for i, val in enumerate(nums)]
print(f"结果(值在前): {indexed_custom2}")
# 输出: [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]

print()


# ========================================
# 五、排序后保留原始编号（重要！）
# ========================================

print("=" * 50)
print("五、排序后保留原始编号（竞赛常用技巧）")
print("=" * 50)

# 示例8：按值排序后，仍能知道原始位置
scores = [85, 92, 78, 95, 88]
print(f"原始数据: {scores}")

# 创建带编号的二维数组 [值, 原始编号]
indexed_scores = [[score, i] for i, score in enumerate(scores, start=1)]
print(f"带编号: {indexed_scores}")

# 按分数降序排序
indexed_scores.sort(reverse=True)
print(f"排序后: {indexed_scores}")
# 输出: [[95, 4], [92, 2], [88, 5], [85, 1], [78, 3]]
# 解释: 原始第4个输入(95分)最高，第2个(92分)第二...

print()
print("排行榜:")
for rank, (score, original_idx) in enumerate(indexed_scores, start=1):
    print(f"第{rank}名: 原第{original_idx}号选手，得分{score}")

print()


# ========================================
# 六、字符串遍历
# ========================================

print("=" * 50)
print("六、字符串遍历")
print("=" * 50)

text = "hello"
for idx, char in enumerate(text):
    print(f"位置 {idx}: '{char}'")
# 输出:
# 位置 0: 'h'
# 位置 1: 'e'
# 位置 2: 'l'
# 位置 3: 'l'
# 位置 4: 'o'

print()


# ========================================
# 七、对比传统写法
# ========================================

print("=" * 50)
print("七、对比传统写法")
print("=" * 50)

items = ['A', 'B', 'C']

print("传统写法（不推荐）:")
for i in range(len(items)):
    print(f"索引 {i}: {items[i]}")

print("\n使用 enumerate（推荐）:")
for i, item in enumerate(items):
    print(f"索引 {i}: {item}")

# 优势：
# 1. 代码更简洁
# 2. 不需要通过索引访问元素
# 3. 性能更好（避免多次索引查找）


# ========================================
# 八、实战练习模板
# ========================================

print("=" * 50)
print("八、实战模板")
print("=" * 50)

"""
# 模板1：输入一行数字，带编号输出
nums = list(map(int, input().split()))
for idx, num in enumerate(nums, start=1):
    print(f"第{idx}个数: {num}")
"""

"""
# 模板2：输入n个数字，排序后输出原始编号
n = int(input())
nums = list(map(int, input().split()))
indexed = [(num, i+1) for i, num in enumerate(nums)]
indexed.sort()  # 按值排序
for num, idx in indexed:
    print(f"原第{idx}位的值: {num}")
"""

"""
# 模板3：与贪心算法结合（类似训练士兵）
n = int(input())
data = []
for i in range(n):
    p, c = map(int, input().split())
    data.append([p, c, i+1])  # [成本, 次数, 原始编号]

data.sort(key=lambda x: x[1])  # 按次数排序
for p, c, idx in data:
    print(f"原第{idx}号: 成本{p}, 次数{c}")
"""

print("\n模板已准备好，取消注释即可使用！")
