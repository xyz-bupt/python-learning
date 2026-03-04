#定义一个类 含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5    #当前手机运行电压

    def  __keep_single_core(self):
        print("保持单核运行")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("可以打5G电话")

        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g，并已设置为单核运行以省电")        


#phone = Phone()
#phone.__keep_single_core()   #调用私有方法,不能使用
#print(phone.__current_voltage)   #调用私有变量,不能使用



#私有成员无法被类对象使用，但是可以被其他的成员使用
phone = Phone()
phone.call_by_5g()   #调用公共方法
