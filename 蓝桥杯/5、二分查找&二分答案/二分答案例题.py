"""
二分答案：
基本模型：“不满足-->满足”模型
答案具有单调增性，即res是check(i)条件进行False/True切换的临界点
"""

def f(x):
    """
    计算三次多项式函数的值
    
    Args:
        x (int | float): 输入数值
    
    Returns:
        int | float: 函数计算结果，即 x³ + x + 1
    """
    return x**3 + x + 1
def bisect(lo , hi, target , check):
    while lo < hi:
        i = (lo + hi) >> 1
        if check(i, target):
            hi = i
        else:
            lo = i + 1
    return lo

target = 99999
res = bisect(1, 10 **18 , target, lambda x, target: f(x) > target)
#找到恰好f(x) > target的地方
print(res)  # 47
print(f(res))  # 103871
print(f(res-1))  # 97383