"""
演示JSON数据和Python字典的相互转换
"""
import json
#准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name":"田所浩二","age":24}, {"name":"我修院","age":25,    "gender":"男"}, {"name":"德川","age":26, "gender":"男"}]
json_str = json.dumps(data,ensure_ascii=False) #将列表转换为JSON字符串
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为JSON
data2 = {"name":"田所浩二","age":24}
json_str = json.dumps(data2,ensure_ascii=False) #将字典转换为JSON字符串
print(type(json_str))
print(json_str)

#将JSON字符串转换为Python数据类型【{k:v,k:v},{}]
s = '[{"name":"田所浩二","age":24}, {"name":"我修院","age":25,    "gender":"男"}, {"name":"德川","age":26, "gender":"男"}]'
data3 = json.loads(s) #将JSON字符串转换为Python数据类型
print(type(data3))
print(data3)

# 将JSON字符串转换为Python数据类型{k:v,k:v}
s2 = '{"name":"田所浩二","age":24}'
data4 = json.loads(s2) #将JSON字符串转换为Python数据类型
print(type(data4))
print(data4)
