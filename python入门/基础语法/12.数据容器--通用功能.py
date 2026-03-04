#演示数据容器的通用功能

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3}


# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大值
print(f"列表 最大值是：{max(my_list)}")
print(f"元组 最大值是：{max(my_tuple)}")
print(f"字符串 最大值是：{max(my_str)}")
print(f"集合 最大值是：{max(my_set)}")
print(f"字典 最大值是：{max(my_dict)}")

# min最小值
print(f"列表 最小值是：{min(my_list)}")
print(f"元组 最小值是：{min(my_tuple)}")
print(f"字符串 最小值是：{min(my_str)}")
print(f"集合 最小值是：{min(my_set)}")
print(f"字典 最小值是：{min(my_dict)}")

# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")  

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}") 

# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}") 

# 进行容器的排序 sorted()
my_list = [3,1,2,5,4]
my_tuple = (5,2,4,1,3)
my_str = "acdbgfe"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key2": 2,"key1": 1,  "key3": 3}

print(f"列表排序的结果是：{sorted(my_list)}")
print(f"元组排序的结果是：{sorted(my_tuple)}")
print(f"字符串排序的结果是：{sorted(my_str)}")
print(f"集合排序的结果是：{sorted(my_set)}")
print(f"字典排序的结果是：{sorted(my_dict)}") 

print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}") 