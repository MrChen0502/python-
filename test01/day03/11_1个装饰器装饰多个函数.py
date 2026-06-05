"""
案例：演示 带参数的装饰器

记忆：
    1.1个装饰器的参数有且只有1一个
    2.如果装饰器有多个参数 可以在该装饰器的外边再包裹一层 把该装饰器当作其 内部函数 返回即可
"""

# 需求 定义1一个既能装饰减法 又能装饰加法的装饰器
# 1.定义装饰器
def logging(flag):
    def my_decorator(fn_name):       # fn_name 原函数名 flag:标记
        # 1.1 定义内部函数 格式要和原函数一样
        def fn_inner(a,b):
            # 1.2 增加额外功能
            if flag == "+":
                print("正在努力计算[加法]中...")
            elif flag == "-":
                print("正在努力计算[减法]中...")
            # 1.3 有引用
            return fn_name(a,b)
        # 1.4 有返回
        return fn_inner
    return my_decorator


# 2.定义原函数 表示 加法运算
@logging("+")
def fn_inner(a,b):
    return a+b


# 3.定义原函数 表示 减法运算
@logging("-")
def get_sub(a,b):
    return a-b