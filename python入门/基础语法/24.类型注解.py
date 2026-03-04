import random
import json
from typing import Union

#变量类型注解

#基础数据类型注解
# var_1: int = 10
# var_2: float = 3.14
# var_3: str = "Hello, World!"
# var_4: bool = True

#类对象类型注解
class Student:
    pass
stu: Student = Student()

#基础容器类型注解
my_list: list = [1, 2, 3, 4, 5]
my_tuple: tuple = (1, "xyz" ,True)
my_set: set = {1, 2, 3, 4, 5}
my_dict: dict = {"name": "Alice", "age": 20}

#容器类型详细注解
my_list: list[int] = [1, 2, 3, 4, 5]
my_tuple: tuple[int, str, bool] = (1, "xyz" ,True)
my_set: set[int] = {1, 2, 3, 4, 5}


#在注释中进行类型注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "zhangsan"}')   # type: dict[str,str]

#类型注解的限制
var_4: int = "itheima"
var_5: str = 123

###################################################################

#函数类型注解


#对形参进行类型注解
def add(x: int, y: int):
    return x + y

#对返回值进行类型注解
def func(data: list):
    return data



#####################################################################
#union类型注解   使用Union[类型,......,类型]   可以定义联合类型注解
my_list: list[Union[int,str]] = [1,2,"itheima","itcast"]

def func(data: Union[int,str]) -> Union[int,str]:
    pass


