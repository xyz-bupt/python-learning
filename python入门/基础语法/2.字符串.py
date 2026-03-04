#定义法：单引号；双引号；三引号
# 在字符串内 包含双引号
name = '"夏北泽先辈"'
print(name)
#在字符串内 包含单引号
nickname = "'114514'"
#转义字符\解除引号效用
name = "\"我叫‘夏北泽先辈’"
print(name)

#字符串拼接
print("Hello," + name + "!" + "你好，" + nickname + "！")   #字符串不能和数字拼接

#字符串格式化
class_num = 57
avg_salary = 114514
message = "田所浩二在%s号会员制餐厅花了%s元钱。" % (class_num, avg_salary)
print(message)

#格式化的精度控制
pi = 3.141592653589793
message = "圆周率的值为%10.5f。" % pi
print (message)

#字符串格式化方式2
name1 = "田所浩二"
number = 114514
print(f"我是{name1},我喜欢的数字是{number}。")

#表达式格式化
print("1 * 1的结果是:%d"% (1*1))
print(f"1 * 1的结果是:{1*1}")
print("字符串在python中的类型是：%s" % type("字符串"))

#输入
print("你是谁")
name = input()
print("你好，" + name + "！")