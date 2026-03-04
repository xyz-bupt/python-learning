#定义字典 键值对
my_dict = {"暴子崇":114,"李田所":514,"杰哥":1}
#定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict},类型：{type(my_dict)}")
print(f"字典2的内容是：{my_dict2},类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型：{type(my_dict3)}")
#定义重复Key的字典 ---不允许重复
my_dict1 = {"暴子崇":114,"李田所":514,"杰哥":1,"暴子崇":0}
print(f"重复key的字典的内容是：{my_dict1}")
#字典同集合一样，不可以使用下标索引，但是可以通过Key值取得对应的Value
num = my_dict["暴子崇"]
print(f"字典中暴子崇对应的数值是：{num}")
#定义嵌套字典
stu_score_dict = {
    "张三":{
        "语文":80,
        "数学":90,
        "英语":85
        },
        "李四":{
            "语文":60,
            "数学":54,
            "英语":45
        },
        "王五":{
            "语文":70,
            "数学":80,
            "英语":100
        }
    }
print(f"学生的考试信息是：{stu_score_dict}")
#从嵌套字典中获取数据
score = stu_score_dict["张三"]["数学"]
print(f"张三的数学成绩是：{score}")    

   #常用操作
#添加元素
my_dict = {"暴子崇":114,"李田所":514,"杰哥":1}
print(f"初始字典：{my_dict}")
my_dict["张三"] = 180
print(f"添加元素后的字典：{my_dict}")
#修改元素
print(f"初始字典：{my_dict}")
my_dict["张三"] = 190    #修改张三的分数为190
print(f"修改元素后的字典：{my_dict}")
#删除元素
score = my_dict.pop("张三")   #删除张三的分数
print(f"字典中被删除了一个元素，结果：{my_dict}，张三的分数是：{score}")
#清空元素,clear()方法
my_dict.clear()
print(f"清空后的字典：{my_dict}")
#获取全部的key
my_dict = {"暴子崇":114,"李田所":514,"杰哥":1}
keys = my_dict.keys()
print(f"字典中所有的key：{keys}")
#遍历字典
 #方式1:通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}，value是：{my_dict[key]}")
 #方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}，value是：{my_dict[key]}")
#统计字典内的元素数量，len()函数
num = len(my_dict)
print(f"字典中元素的数量是：{num}")


# ========================================
# 字典高级用法补充
# ========================================

print("\n" + "="*50)
print("字典高级用法补充")
print("="*50)

# 1. get() 方法 - 安全获取值
my_dict = {"暴子崇":114,"李田所":514,"杰哥":1}
print(f"\n原始字典: {my_dict}")

# 键存在，返回对应值
print(f"get获取存在的key: {my_dict.get('暴子崇')}")  # 输出: 114

# 键不存在，返回 None（不报错）
print(f"get获取不存在的key: {my_dict.get('张三')}")  # 输出: None

# 键不存在，返回指定默认值
print(f"get获取不存在的key(带默认值): {my_dict.get('张三', 0)}")  # 输出: 0

# 对比直接访问（键不存在会报错）
# print(my_dict['张三'])  # KeyError: '张三'

# 2. items() 方法 - 获取所有键值对
print("\n--- items() 方法 ---")
my_dict = {"a": 1, "b": 2, "c": 3}
items = my_dict.items()
print(f"所有键值对: {items}")  # 输出: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 遍历键值对（最常用的方式！）
print("遍历键值对:")
for key, value in my_dict.items():
    print(f"  {key}: {value}")
# 输出:
#   a: 1
#   b: 2
#   c: 3

# 3. values() 方法 - 获取所有值
print("\n--- values() 方法 ---")
values = my_dict.values()
print(f"所有值: {values}")  # 输出: dict_values([1, 2, 3])
print(f"转为列表: {list(values)}")  # 输出: [1, 2, 3]

# 4. keys() 方法 - 获取所有键
print("\n--- keys() 方法 ---")
keys = my_dict.keys()
print(f"所有键: {keys}")  # 输出: dict_keys(['a', 'b', 'c'])
print(f"转为列表: {list(keys)}")  # 输出: ['a', 'b', 'c']

# 5. 字典推导式
print("\n--- 字典推导式 ---")
# 示例：生成平方数字典
squares = {x: x**2 for x in range(1, 6)}
print(f"平方数字典: {squares}")  # 输出: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 示例：筛选字典（只保留值大于2的）
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v > 2}
print(f"筛选后(值>2): {filtered}")  # 输出: {'c': 3, 'd': 4}

# 示例：交换键值
swapped = {v: k for k, v in original.items()}
print(f"交换键值: {swapped}")  # 输出: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 6. 判断键是否存在
print("\n--- 判断键是否存在 ---")
my_dict = {"name": "Alice", "age": 25}
print(f"'name' in dict: {'name' in my_dict}")  # 输出: True
print(f"'city' in dict: {'city' in my_dict}")  # 输出: False

# 7. setdefault() 方法 - 键不存在时设置默认值
print("\n--- setdefault() 方法 ---")
my_dict = {"a": 1}
# 键存在，返回原值
print(f"setdefault存在的key: {my_dict.setdefault('a', 99)}")  # 输出: 1
print(f"字典: {my_dict}")  # {'a': 1}

# 键不存在，设置默认值并返回
print(f"setdefault不存在的key: {my_dict.setdefault('b', 2)}")  # 输出: 2
print(f"字典: {my_dict}")  # {'a': 1, 'b': 2}

# 8. update() 方法 - 更新字典
print("\n--- update() 方法 ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}  # b会覆盖，c是新增
dict1.update(dict2)
print(f"更新后: {dict1}")  # 输出: {'a': 1, 'b': 20, 'c': 3}

# 9. fromkeys() 方法 - 创建相同值的字典
print("\n--- fromkeys() 方法 ---")
keys = ['a', 'b', 'c']
# 所有键的值都设为 0
dict_from_keys = dict.fromkeys(keys, 0)
print(f"fromkeys结果: {dict_from_keys}")  # 输出: {'a': 0, 'b': 0, 'c': 0}

# 10. popitem() 方法 - 删除并返回最后一个键值对
print("\n--- popitem() 方法 ---")
my_dict = {"a": 1, "b": 2, "c": 3}
key, value = my_dict.popitem()
print(f"删除的键值对: {key}, {value}")  # 输出: c, 3
print(f"删除后: {my_dict}")  # 输出: {'a': 1, 'b': 2}


# ========================================
# defaultdict - 带默认值的字典
# ========================================

print("\n" + "="*50)
print("defaultdict - 带默认值的字典")
print("="*50)

from collections import defaultdict

# 1. 默认值为空列表（用于分组）
print("\n--- 默认值为空列表 ---")
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(f"分组结果: {dict(d)}")  # 输出: {'a': [1, 2], 'b': [3]}
print(f"访问不存在的key: {d['c']}")  # 输出: []（不报错！）

# 2. 默认值为 int（用于计数）
print("\n--- 默认值为 int（计数） ---")
s = "hello"
count = defaultdict(int)
for char in s:
    count[char] += 1
print(f"字符统计: {dict(count)}")  # 输出: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 3. 默认值为 set（用于去重分组）
print("\n--- 默认值为 set（去重分组） ---")
d = defaultdict(set)
d['a'].add(1)
d['a'].add(1)  # 重复值不会添加
d['a'].add(2)
d['b'].add(3)
print(f"去重分组: {dict(d)}")  # 输出: {'a': {1, 2}, 'b': {3}}

# 4. 按条件分组（实战应用）
print("\n--- 按条件分组实战 ---")
students = [
    ('张三', 'A班'),
    ('李四', 'B班'),
    ('王五', 'A班'),
    ('赵六', 'B班'),
]
class_group = defaultdict(list)
for name, cls in students:
    class_group[cls].append(name)
print(f"按班级分组:")
for cls, names in class_group.items():
    print(f"  {cls}: {names}")
# 输出:
#   A班: ['张三', '王五']
#   B班: ['李四', '赵六']


# ========================================
# 实战应用示例
# ========================================

print("\n" + "="*50)
print("实战应用示例")
print("="*50)

# 1. 统计词频
print("\n--- 统计词频 ---")
text = "hello world hello python"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"词频统计: {word_count}")
# 输出: {'hello': 2, 'world': 1, 'python': 1}

# 2. 分组计算
print("\n--- 分组计算（按类别求和） ---")
sales = [
    ('苹果', 100),
    ('香蕉', 50),
    ('苹果', 80),
    ('香蕉', 60),
]
category_sum = defaultdict(int)
for item, amount in sales:
    category_sum[item] += amount
print(f"类别销售额:")
for item, total in category_sum.items():
    print(f"  {item}: {total}")
# 输出:
#   苹果: 180
#   香蕉: 110

# 3. 嵌套字典访问
print("\n--- 嵌套字典操作 ---")
stu_scores = {
    "张三": {"语文": 80, "数学": 90},
    "李四": {"语文": 60, "数学": 54},
}
# 添加新科目成绩
stu_scores["张三"]["英语"] = 85
# 修改成绩
stu_scores["李四"]["语文"] = 70
print(f"更新后: {stu_scores}")


# ========================================
# 字典方法速查表
# ========================================

print("\n" + "="*50)
print("字典方法速查表")
print("="*50)

methods_table = """
┌─────────────────┬────────────────────────────────┐
│      方法       │           说明                 │
├─────────────────┼────────────────────────────────┤
│ d[key]          │ 获取值，键不存在则报错          │
│ d.get(key)      │ 安全获取，不存在返回 None       │
│ d.get(key, def) │ 安全获取，不存在返回 def        │
│ d[key] = val    │ 添加/修改键值对                 │
│ d.pop(key)      │ 删除键并返回值                  │
│ d.popitem()     │ 删除并返回最后一个键值对         │
│ d.keys()        │ 获取所有键                      │
│ d.values()      │ 获取所有值                      │
│ d.items()       │ 获取所有键值对                  │
│ d.clear()       │ 清空字典                        │
│ d.update(other) │ 用 other 更新字典               │
│ d.setdefault()  │ 键不存在时设置默认值            │
│ dict.fromkeys() │ 创建相同值的字典                │
│ key in d        │ 判断键是否存在                  │
│ len(d)          │ 字典元素数量                    │
└─────────────────┴────────────────────────────────┘
"""
print(methods_table)
