#逆波兰表达式：操作符置于操作数的后面
"""
中缀表达式： a + b
前缀表达式:  + a b
后缀表达式:  a b +
"""

def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),  # 关键：向0取整（而非python默认的向下取整）
    }

    for t in tokens:
        if t in ops:
            y = stack.pop()
            x = stack.pop()
            stack.append(ops[t](x, y))   #注意操作数顺序：a在前，b在后
        else:
            stack.append(int(t))
    return stack[0]

"""
在 Python 中：
/ 表示真除法，结果是浮点数（即使两个整数相除也会得到小数）
print(5 / 2)   # 输出 2.5
print(-3 / 2)  # 输出 -1.5

// 表示整除（向下取整，floor），结果是整数（如果参与运算的是整数）或浮点数（如果有小数）
print(5 // 2)   # 输出 2
print(-3 // 2)  # 输出 -2

"""
#向0取整
print(int(5 / 2))    # 输出 2
print(int(-3 / 2))   # 输出 -1