"""
案例：装饰器_无参无返回的原函数

细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即:原函数是无参无返回的 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回 则 装饰器的内部函数也必须是 有参有返回的
"""

# 需求：定义无参无返回值的get_sum()求和函数 在不改变其代码的基础上 添加友好提示 正在努力计算ing
# 1.定义装饰器
def my_decorator(fn_name):
    # 1.1 定义内部函数 其格式必须和被装饰的原函数 保持一致
    def fn_inner():
        # 1.2 添加提示信息
        print("正在努力计算ing...")
        fn_name()
    # 1.4 返回内部函数(对象)
    return fn_inner

# 2.定义原函数
@my_decorator    # num = my_decorator(get_sum)
def get_sum():
    a = 10
    b = 20
    sum = a +b
    print(f"sum求和结果:{sum}")

# 3. 测试
# 3.1 传统方式
num = my_decorator(get_sum)
num()

# 3.2 语法糖
get_sum()