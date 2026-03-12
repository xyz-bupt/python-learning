#threading模块实现多线程编程


"""
import threading

thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
 - group：暂时无用，未来功能的预留参数
 - target：执行的目标任务名
 - args：以元组的方式给任务传参
 - kwargs：以字典的方式给任务传参
 - name：线程名，一般不用设置

"""

import threading
import time

def sing():
    while True:
        print("唱歌")
        time.sleep(1)


def dance():
    while True:
        print("跳舞")
        time.sleep(1)


if __name__ == '__main__':
    #创建一个唱歌的线程
    sing_thread = threading.Thread(target = sing)
    #创建一个跳舞的线程
    dance_thread = threading.Thread(target = dance)
    #启动所有线程
    sing_thread.start()
    dance_thread.start()


"""
需要传参可以通过：
- args参数通过元组（按参数顺序)的方式传参
- kwargs参数通过字典的方式传参
"""

