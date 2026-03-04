#闭包：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包

#简单闭包
#

#使用nonlocal关键字修改外部函数的值
""" def outer(num1):

    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner

fn = outer(10)
fn(10)
fn(10)
fn(10)
 """

#实现atm取钱小案例
def account_create(initial_amount=0):  #initial_amount不会被外部篡改，保证安全

    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款： +{num}, 余额：{initial_amount}")

        else:
            initial_amount -= num
            print(f"取款： -{num}, 余额：{initial_amount}")

    return atm

atm = account_create(114)

atm(100)
atm(200)
atm(100, deposit=False)