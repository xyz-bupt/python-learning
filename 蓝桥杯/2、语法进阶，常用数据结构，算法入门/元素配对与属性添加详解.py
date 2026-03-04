"""
========================================
元素配对与属性添加详解
========================================

本文档讲解如何给输入的元素添加额外属性（编号、权重等）
适用于：贪心算法排序后保留原始位置、数据处理等场景
"""

# ========================================
# 方法一：enumerate - 自动生成索引
# ========================================

print("=" * 60)
print("方法一：enumerate() - 自动索引（最简单）")
print("=" * 60)

nums = [10, 20, 30, 40, 50]

# 从0开始自动编号
result = list(enumerate(nums))
print(f"从0开始: {result}")
# 输出: [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]

# 从1开始自动编号
result = list(enumerate(nums, start=1))
print(f"从1开始: {result}")
# 输出: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

# 调整格式：值在前，编号在后
result = [(val, i) for i, val in enumerate(nums, start=1)]
print(f"值在前: {result}")
# 输出: [(10, 1), (20, 2), (30, 3), (40, 4), (50, 5)]

print()


# ========================================
# 方法二：zip - 组合多个列表
# ========================================

print("=" * 60)
print("方法二：zip() - 组合多个列表的对应元素")
print("=" * 60)

values = [10, 20, 30]
ids = [100, 200, 300]
weights = [1.5, 2.5, 3.5]

# 两两配对
result = list(zip(ids, values))
print(f"编号+值: {result}")
# 输出: [(100, 10), (200, 20), (300, 30)]

# 三个列表组合
result = list(zip(values, ids, weights))
print(f"值+编号+权重: {result}")
# 输出: [(10, 100, 1.5), (20, 200, 2.5), (30, 300, 3.5)]

# 转换为列表形式（可修改）
result = [[v, i, w] for v, i, w in zip(values, ids, weights)]
print(f"列表形式: {result}")
# 输出: [[10, 100, 1.5], [20, 200, 2.5], [30, 300, 3.5]]

print()


# ========================================
# 方法三：循环中手动添加属性
# ========================================

print("=" * 60)
print("方法三：循环中手动添加属性（最灵活）")
print("=" * 60)

n = 5
data = []

# 场景：读取 n 个数据，每个数据有值和编号
for i in range(1, n + 1):
    value = i * 10  # 模拟输入：10, 20, 30, 40, 50
    data.append([value, i])  # [值, 编号]

print(f"数据: {data}")
# 输出: [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]

# 添加更多属性
n = 3
data = []
for i in range(1, n + 1):
    value = i * 10
    weight = i * 0.5
    priority = i
    data.append([value, weight, priority, i])  # [值, 权重, 优先级, 编号]

print(f"多属性: {data}")
# 输出: [[10, 0.5, 1, 1], [20, 1.0, 2, 2], [30, 1.5, 3, 3]]

print()


# ========================================
# 方法四：字典结构 - 可读性最好
# ========================================

print("=" * 60)
print("方法四：字典结构 - 属性有名称（推荐用于复杂对象）")
print("=" * 60)

values = [10, 20, 30]
names = ['A', 'B', 'C']

result = [
    {'value': v, 'name': n, 'id': i+1}
    for i, (v, n) in enumerate(zip(values, names))
]
print(result)
# 输出: [
#   {'value': 10, 'name': 'A', 'id': 1},
#   {'value': 20, 'name': 'B', 'id': 2},
#   {'value': 30, 'name': 'C', 'id': 3}
# ]

# 访问属性
print(f"第一个元素的值: {result[0]['value']}")
print(f"第二个元素的名字: {result[1]['name']}")

print()


# ========================================
# 实战场景1：贪心算法 - 排序后保留原位置
# ========================================

print("=" * 60)
print("实战1：贪心算法 - 排序后找回原始位置")
print("=" * 60)

# 输入：5个学生的分数
scores = [85, 92, 78, 95, 88]
print(f"原始分数: {scores}")

# 方法A：使用 enumerate（推荐）
indexed = [(score, idx) for idx, score in enumerate(scores, start=1)]
indexed.sort(reverse=True)  # 按分数降序

print("\n排行榜（使用 enumerate）:")
for rank, (score, idx) in enumerate(indexed, start=1):
    print(f"第{rank}名: 原第{idx}位学生，得分{score}")

# 方法B：循环添加编号
indexed = []
for i, score in enumerate(scores, start=1):
    indexed.append([score, i])
indexed.sort(reverse=True)

print("\n排行榜（循环添加）:")
for rank, item in enumerate(indexed, start=1):
    print(f"第{rank}名: 原第{item[1]}位学生，得分{item[0]}")

print()


# ========================================
# 实战场景2：输入多列数据
# ========================================

print("=" * 60)
print("实战2：输入多列数据（类似训练士兵问题）")
print("=" * 60)

# 模拟输入：每行两个数（成本、次数）
# 输入:
# 10 2
# 20 5
# 30 3
# 40 4
# 50 1

raw_data = [[10, 2], [20, 5], [30, 3], [40, 4], [50, 1]]

# 添加编号
data = []
for i, (p, c) in enumerate(raw_data, start=1):
    data.append([p, c, i])  # [成本, 次数, 编号]

print(f"带编号数据: {data}")
# 输出: [[10, 2, 1], [20, 5, 2], [30, 3, 3], [40, 4, 4], [50, 1, 5]]

# 按次数排序
data.sort(key=lambda x: x[1])  # 按第二个元素（次数）排序
print(f"按次数排序: {data}")
# 输出: [[50, 1, 5], [10, 2, 1], [30, 3, 3], [40, 4, 4], [20, 5, 2]]

# 解析结果
print("\n排序后解析:")
for p, c, idx in data:
    print(f"原第{idx}号: 成本{p}, 次数{c}")

print()


# ========================================
# 实战场景3：加权计算
# ========================================

print("=" * 60)
print("实战3：加权计算")
print("=" * 60)

values = [10, 20, 30, 40]
weights = [2, 3, 1, 4]

# 组合并计算加权和
weighted_sum = 0
result = []
for v, w in zip(values, weights):
    result.append([v, w, v * w])  # [值, 权重, 加权结果]
    weighted_sum += v * w

print("加权明细:")
for item in result:
    print(f"值{item[0]} × 权重{item[1]} = {item[2]}")
print(f"\n加权和: {weighted_sum}")

print()


# ========================================
# 方法对比总结
# ========================================

print("=" * 60)
print("方法对比总结")
print("=" * 60)

print("""
┌─────────────┬──────────────────┬────────────────────────┐
│    方法     │     适用场景     │        代码示例         │
├─────────────┼──────────────────┼────────────────────────┤
│ enumerate   │ 自动连续编号     │ [(i,val) for i,val in  │
│             │                  │  enumerate(nums,1)]    │
├─────────────┼──────────────────┼────────────────────────┤
│ zip         │ 组合多个列表     │ list(zip(vals, ids))   │
├─────────────┼──────────────────┼────────────────────────┤
│ 循环添加    │ 复杂逻辑/多属性   │ [[v,w,p,i] for i,v in  │
│             │                  │  enumerate(vals)]      │
├─────────────┼──────────────────┼────────────────────────┤
│ 字典        │ 属性多/可读性要求 │ [{'val':v,'id':i} ...] │
└─────────────┴──────────────────┴────────────────────────┘
""")

print("\n推荐选择：")
print("  - 简单编号 → enumerate()")
print("  - 多列表组合 → zip()")
print("  - 复杂属性 → 循环添加 + 列表")
print("  - 可读性优先 → 字典")


# ========================================
# 代码模板（直接可用）
# ========================================

print("\n" + "=" * 60)
print("常用代码模板（取消注释使用）")
print("=" * 60)

"""
# 模板1：一行输入，自动编号
nums = list(map(int, input().split()))
indexed = [(num, i+1) for i, num in enumerate(nums)]
"""

"""
# 模板2：多行输入，每行添加编号
n = int(input())
data = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    data.append([a, b, i])  # [值1, 值2, 编号]
"""

"""
# 模板3：两个列表配对
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
paired = list(zip(values, weights))
"""

"""
# 模板4：排序后保留原位置（竞赛常用）
nums = list(map(int, input().split()))
indexed = [(num, i) for i, num in enumerate(nums)]
indexed.sort()  # 按值排序
for num, idx in indexed:
    print(f"原第{idx+1}位: {num}")
"""

print("\n模板已准备好，根据需要取消注释使用！")
