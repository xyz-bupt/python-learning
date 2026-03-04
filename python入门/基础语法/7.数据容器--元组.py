#元组：一旦定义完成不可修改  (1,2,3,4,5)
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print (f"t1的类型是：{type(t1)},内容是：{t1}")
print (f"t2的类型是：{type(t2)},内容是：{t2}")
print (f"t3的类型是：{type(t3)},内容是：{t3}")
#元组的嵌套
t4 = ((1,2,3),(4,5,6))
print (f"t4的类型是：{type(t4)},内容是：{t4}")
#下标索引取出内容
num = t4[1][2]
print (f"t4的第2个元素的第3个元素是：{num}")
#元组的操作
t5 = ("下北泽","野兽先辈","会员制餐厅","下北泽")
index = t5.index("会员制餐厅")
print (f"t5的第{index+1}个元素是：{t5[index]}")
t5.count("下北泽")
print (f"t5中出现了{t5.count('下北泽')}次‘下北泽’")
num = len(t5)
print (f"t5的元素个数是：{num}")
#遍历——while循环
index = 0
while index < len(t5):
    print (f"t5的第{index+1}个元素是：{t5[index]}")
    index += 1
#遍历——for循环
for item in t5:
    print (f"t5的元素是：{item}")
 #修改元组内容——不可修改，但可以修改元组内的list的内容
t6 = (1,2,['114','514'])
t6[2][1] = '1919810'
print (t6)

