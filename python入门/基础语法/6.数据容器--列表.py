#列表，元组，字符串，字典，集合
#列表
name_list = ['Alice', 'Bob', 'Charlie']
print(name_list)
print(type(name_list))
#嵌套列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(type(nested_list))
#下标索引
print(nested_list[0])
#常用操作
#查找某元素在列表捏的下标索引
index = name_list.index('Bob')
print(index)
#修改特定下标索引的值
name_list[1] = 'David'
print(name_list)
#插入元素
name_list.insert(1, 'Eve')
print(name_list)
#追加元素
name_list.append('Frank')
print(name_list)
#追加一批元素
name_list.extend(['Grace', 'Henry'])
print(name_list)
#删除指定下标索引的元素（两种方式）
 #方法1：pop()方法
deleted_element = name_list.pop(2)
print(name_list)
print(f"我已经删除了{deleted_element}这个元素")
 #方法2：del语句
del name_list[2]
print(name_list)
#删除某元素在列表中的第一个匹配项
name_list.remove('Eve')
print(name_list)
#清空列表
name_list.clear()
print(name_list)
#统计列表内某元素的数量
name_list = ['Alice', 'Eve', 'David', 'Charlie', 'Frank','Eve', 'Grace', 'Henry']
count = name_list.count('Eve')
print(count)
#统计列表中全部的元素数量
length = len(name_list)
print(f"列表总共有{length}个元素")
#循环遍历——while
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
print ("循环结束")    
#循环遍历——for
for name in name_list:
    print(name)
print("循环结束")    