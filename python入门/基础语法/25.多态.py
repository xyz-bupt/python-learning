#多态：多种状态，在完成某个行为时，使用不同的对象会得到不同的状态

class Animal:    #抽象类
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    #制造噪音，需要传入animal对象
    animal.speak()


#演示多态，使用两个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)  #输出：汪汪汪
make_noise(cat)  #输出：喵喵喵