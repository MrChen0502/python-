"""
案例：nonlocal关键字介绍

nonlocal：
    它是python内置的关键字 可以实现 在内部函数中 修改外部函数的 变量值
"""

# 需求：编写一个闭包 让内部函数访问外部函数的参数 a = 100 并观察结果

# 1.定义外部函数
def fn_outer():
    # 2.定义外部函数的(局部变量)变量
    a = 100

    # 3.定义内部函数 访问外部函数的变量
    def fn_inner():
        # 在内部函数中访问外部函数的变量
        nonlocal a
        a += 1
        # 5.打印外部函数的变量
        print(f"a:{a}")
    return fn_inner

if __name__ == '__main__':
    f = fn_outer()
    f()
    f()
    f()
