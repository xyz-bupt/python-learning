my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(value)
print(value2)  #从前向后，下标从0开始；从后向前，下标从-1开始
#同元组一样，字符串是一个无法修改的数据容器
#index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找'and'的位置，其起始下标是{value}")
#字符串的替换
new_str = my_str.replace("itcast", "python")
print(f"将字符串{my_str}替换后得到:{new_str}")
#split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到:{my_str_list}, 类型是：{type(my_str_list)}"  )
#字符串的规整操作 strip方法
my_str = "      hello python itheima itcast  "
new_str = my_str.strip()  #不传入参数，去除首尾空格
print(f"将字符串{my_str}进行strip规整后得到:{new_str}")

my_str = "12下北泽先辈21"
new_str = my_str.strip("12")  #去除指定字符
print(f"将字符串{my_str}进行strip('12')后得到:{new_str}")

#统计字符串中某字符串的出现次数 count
my_str = "hello python itheima itcast itheima"
count = my_str.count("it")
print(f"字符串{my_str}中出现'it'的次数是:{count}")
#统计字符串的长度 len()
num = len(my_str)
print(f"字符串{my_str}的长度是:{num}")