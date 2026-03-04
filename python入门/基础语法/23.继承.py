# class 类名（父类名）

#单继承
class Phone:
    IMEI = None  #序列号
    producer = "HM"  #制造商


    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"   #面部识别id


    def call_by_5g(self):
        print("新功能 5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


#多继承
#    class 类名（父类名1，父类名2，...）：
#     pass (语法补全)

#多个父类中，相同的方法名，只会调用第一个父类的方法（从左到右） 先继承的保留，后继承的覆盖



#复写  （子类中重新定义同名属性或方法即可）
#调用父类同名成员：1.父类名.成员变量/成员方法(self)  2.super().成员变量/成员方法()