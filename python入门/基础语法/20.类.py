
#定义在类内部的函数叫"方法"

#设计一个类
class Student:
    name = None
    gender = None
    nationality = None 
    native_place = None
    age = None
    def say_hi(self):
        print("Hello, my name is " + self.name)
        print(f"I am {self.age} years old.")

#创建一个对象
stu_1 = Student()

#对象属性进行赋值
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "北京"
stu_1.age = 20

#获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.native_place)
print(stu_1.age)        

stu_1.say_hi()

a = input("请输入")
print(a)