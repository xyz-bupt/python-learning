from typing import List

"""
========================================
两数之和 (Two Sum) - 哈希表解法
========================================

题目：给定一个整数数组 nums 和一个整数 target，
      在数组中找出和为 target 的两个整数，返回它们的索引。

示例：
    输入：nums = [2, 7, 11, 15], target = 9
    输出：[0, 1]  （因为 nums[0] + nums[1] = 2 + 7 = 9）
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表解法（前缀哈希）

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        # d = {数值: 索引}
        d = {}
        n = len(nums)

        for i, x in enumerate(nums):
            # 检查 target - x 是否已存在于字典中
            if d.get(target - x) is not None:
                return [i, d[target - x]]
            # 没找到，将当前数存入字典
            d[x] = i


# ========================================
# 代码详解
# ========================================

print("=" * 50)
print("代码逐行讲解")
print("=" * 50)

print("""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}                    # 创建空字典，存储 {数值: 索引}
        n = len(nums)            # 获取数组长度（这里其实没用上）

        for i, x in enumerate(nums):           # 遍历数组，i是索引，x是值
            if d.get(target - x) is not None:  # 检查配对值是否在字典中
                return [i, d[target - x]]      # 找到！返回两个索引
            d[x] = i                            # 没找到，存入当前值和索引
""")


# ========================================
# 执行过程演示
# ========================================

print("\n" + "=" * 50)
print("执行过程演示")
print("=" * 50)

nums = [2, 7, 11, 15]
target = 9

print(f"\n输入: nums = {nums}, target = {target}\n")

d = {}
for i, x in enumerate(nums):
    complement = target - x
    print(f"第{i}步: nums[{i}] = {x}")
    print(f"  → 寻找配对: {target} - {x} = {complement}")
    print(f"  → 字典: {d}")

    if d.get(complement) is not None:
        print(f"  ✓ 找到了！{x} + {complement} = {target}")
        print(f"  ✓ 返回: [{i}, {d[complement]}]\n")
        break
    else:
        print(f"  × 配对 {complement} 不在字典中")
        print(f"  → 存入: d[{x}] = {i}\n")
    d[x] = i


# ========================================
# 核心思路
# ========================================

print("\n" + "=" * 50)
print("核心思路")
print("=" * 50)

print("""
问题：如何快速知道 target - x 是否在数组中？

暴力法：对每个元素，遍历后面所有元素查找
        时间复杂度：O(n²)

哈希法：
  1. 用字典存储已经遍历过的元素 {值: 索引}
  2. 对当前元素 x，检查 target - x 是否在字典中
  3. 在 → 找到配对，返回索引
  4. 不在 → 将 x 存入字典，继续

为什么快？
  - 字典的查找操作 d.get(key) 时间复杂度是 O(1)
  - 只需遍历一次数组
  - 总时间复杂度：O(n)
""")


# ========================================
# 关键点说明
# ========================================

print("\n" + "=" * 50)
print("关键点说明")
print("=" * 50)

print("""
1. 字典存什么？
   d = {数值: 索引}
   这样找到配对值时，可以直接返回它的索引

2. 为什么要先查找再存入？
   如果先存入，可能自己和自己配对
   例如：target=4，当前x=2，会错误地返回 [i, i]

3. d.get(target - x) is not None 是什么意思？
   - get() 找不到时返回 None
   - 配对值可能是 0，所以不能用 if not d.get(...)
   - 用 is not None 判断更严谨

4. 为什么叫"前缀哈希"？
   - "前缀"：只看当前位置之前的元素
   - "哈希"：使用哈希表（字典）存储
   - 是一种常见技巧：边遍历边查询已遍历的元素
""")


# ========================================
# 代码模板
# ========================================

print("\n" + "=" * 50)
print("通用模板：在数组中找配对")
print("=" * 50)

template = """
# 基础模板：返回索引
def twoSum(nums, target):
    d = {}  # {值: 索引}
    for i, x in enumerate(nums):
        if target - x in d:      # 查找配对
            return [i, d[target - x]]
        d[x] = i                 # 存入当前元素


# 变体1：只判断配对是否存在
def hasPair(nums, target):
    seen = set()  # 只需判断存在，用 set
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False


# 变体2：统计配对数量
def countPairs(nums, target):
    d = {}
    count = 0
    for x in nums:
        if target - x in d:
            count += d[target - x]
        d[x] = d.get(x, 0) + 1
    return count
"""
print(template)
