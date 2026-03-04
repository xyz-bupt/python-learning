#导入自定义的包中的模块，并使用
import my_package.my_module1 

my_package.my_module1.test(1,3)

from my_package.my_module2 import test_a

test_a(2,4)

#方式2： from 包名 import* 模块名.目标
#注意：必须在“__init__.py"文件中添加"__all__ = []" , 控制允许导入的模块列表