#定义集合
my_set = {"田所浩二","淳平","德川","我修院","田所浩二","淳平","德川","我修院"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")
#无序，不支持下标索引，允许修改
#添加新元素 add()
my_set.add("暴子崇")
print(f"添加新元素后，my_set的内容是：{my_set}")
#移除元素 remove()
my_set.remove("田所浩二")
print(f"移除元素后，my_set的内容是：{my_set}")
#随机取出一个元素 pop()
print(f"随机取出一个元素：{my_set.pop()}")
print(f"my_set的内容是：{my_set}")
#清空集合 clear()
my_set.clear()
print(f"清空集合后，my_set的内容是：{my_set}")
#取两个集合的差集 difference()
#语法：set1.difference(set2) 功能：返回set1中不包含在set2中的元素组成的集合（集合1和集合2的差集）
set1 = {"田所浩二","淳平","德川","我修院"}
set2 = {"暴子崇","淳平","我修院","田所浩二"}
print(f"set1的差集是：{set1.difference(set2)}")
print(f"set2的差集是：{set2.difference(set1)}")
#消除两个集合的差集 difference_update()
#语法：set1.difference_update(set2) 功能：对比集合1和集合2，在集合1内删除和集合2相同的元素
#结果：集合1被修改，集合2不变
set1 = {"田所浩二","淳平","德川","我修院"}
set2 = {"暴子崇","淳平","我修院","田所浩二"}
set1.difference_update(set2)
print(f"取差集后，set1的内容是：{set1}")
#两个集合合并为一个集合 union()
#语法：set1.union(set2) 功能：返回两个集合的并集（集合1和集合2的并集）
#结果：得到新集合，集合1和集合2不变
set1 = {"田所浩二","淳平","德川","我修院"}
set2 = {"暴子崇","淳平","我修院","田所浩二"}
print(f"两个集合的并集是：{set1.union(set2)}")
#统计集合元素数量 len()
set1 = {"田所浩二","淳平","德川","我修院"}
print(f"set1的元素数量是：{len(set1)}")
#集合的遍历
#集合不支持下标索引，不支持while循环，但是支持for循环
set1 = {"田所浩二","淳平","德川","我修院"}
for item in set1:
    print(f"集合的元素有：{item}")
