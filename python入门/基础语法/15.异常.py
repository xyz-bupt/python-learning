#异常——bug
#捕获异常
#基本语法：try: 可能发生异常的代码块 except: 如果发生异常执行的代码
# try:
#     f = open('暴子崇.txt', 'r')
# except :
#     print("出现异常，文件不存在，将改为w模式打开")
#     f = open("暴子崇.txt", "w")

#捕获指定异常
try:
     print(fuck)
except NameError as e:
    print("出现了变量未定义的异常")

#捕获多个异常
try:
     1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或除数为零的异常")    
 
try:
     1/0
except Exception as e:
    print("出现了异常")  

#异常else else表示的是如果没有异常要执行的代码
try:
    print("hello")
except:
    print("出现异常")
else:
    print("没有异常")

#异常的finally    finally: 
#无论是否异常都要执行

#异常的传递性
def func1():
    print("func1开始执行")
    num = 1/0     #肯定有异常（除以0）
    print("func1执行结束")

def func2():
    print("func2开始执行")
    func1()
    print("func2执行结束")

def main ():
   try:
    func2()

   except Exception as e:
    print(f"出现了异常，异常的信息是：{e}")
main()