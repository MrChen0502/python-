"""
案例：装饰器_有参有返回的原函数

细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即:原函数是无参无返回的 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回 则 装饰器的内部函数也必须是 有参有返回的
"""

# 需求：定义有参有返回值的get_sum()求和函数 在不改变其代码的基础上 添加友好提示 正在努力计算ing
# 1.定义装饰器
def my_decorator(fn_name):
    # 1.1 定义内部函数
    def fn_inner(a,b):
        # 1.2 额外功能
        print("正在努力计算ing")
        # 1.3 调用原函数
        return fn_name(a,b)
    # 1.4 返回内部函数
    return fn_inner

# 2.定义原函数
@my_decorator
def get_sum(a , b):
    return a + b

# 3. 测试
# 3.1 传统方式
get_sum = my_decorator(get_sum)  # 本质 get_sum = fn_inner
sum = get_sum(1,1)
print(f"求和结果是:{sum}")

# 3.2 语法糖
print(f"求和结果是:{get_sum(1,1)}")