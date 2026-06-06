"""
案例：深浅拷贝

记忆(总结)：
    1.所谓的深浅拷贝分别指的是
        浅拷贝：copy模块的copy()
        深拷贝：copy模块的deepcopy()函数
    2.大白话解释深浅拷贝：
        深拷贝拷贝的多 浅拷贝拷贝的少
    3.深拷贝主要是针对于可变类型来讲的 深拷贝拷贝所有层（可变类型） 浅拷贝只拷贝第一层（可变类型）
      如果是针对于不可变类型 则用法和普通赋值一样 并无区别
"""


def dm01_普通赋值():

    # 普通赋值 不可变类型
    a = 10
    b = a

    print('id(a)→', id(a))  # 0x01
    print('id(b)→', id(b))  # 0x01
    print('id(10)→', id(10))  # 0x01

    # 普通赋值 可变类型
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [a, b]
    d = c

    print('id(c)→', id(c))  #
    print('id(d)→', id(d))  #



import copy

def dm02_浅拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]

    d = copy.copy(c)

    print('id(c)→', id(c))
    print('id(d)→', id(d))

    # 测试2
    print(id(c[2]))
    print(id(a))

    # 修改a[2] = 22
    a[2] = 22
    # c[0] = 100
    print('c→', c)
    print('d→', d)

import copy

def dm03_浅拷贝不可变类型():
    # 不可变类型 a b c
    a = (1, 2, 3)        # 0x01
    b = (11, 22, 33)     # 0x02
    c = (6, 7, a, b)     # 0x03

    d = copy.copy(c)

    print('id(c)→', id(c))  # 0x03
    print('id(d)→', id(d))  # 0x03


import copy


def dm04_深拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]

    d = copy.deepcopy(c)

    print('id(c)→', id(c))  # 比如 0x100
    print('id(d)→', id(d))  # 比如 0x200 (不同)

    a[1] = 100
    b[1] = 800

    print(f'c: {c}')  # c: [6, 7, [1, 100, 3], [11, 800, 33]]
    print(f'd: {d}')  # d: [6, 7, [1, 2, 3], [11, 22, 33]] (没变！)

    import copy

def dm05_深拷贝不可变类型():
    a = (1, 2, 3)
    b = (11, 22, 33)
    c = (a, b)

    d = copy.deepcopy(c)
    print(id(c))  #
    print(id(d))  #



if __name__ == '__main__':
    # dm01_普通赋值()
    # dm02_浅拷贝可变类型()
    # dm03_浅拷贝不可变类型()
    # dm04_深拷贝可变类型()
    dm03_浅拷贝不可变类型()