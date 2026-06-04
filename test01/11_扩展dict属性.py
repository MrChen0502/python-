"""
案例： 演示python内置的dict属性

__dict__ 属性介绍：
    它是python内置的属性 可以把对象转成字典形式
"""
# 导包
from StudentCMS.student import Student

# 需求1：把 学生对象 ——> 字典形式 属性名做键 属性值做值
# s1 = Student("11","111","1111","11111","111111")

# 需求2 把[学生对象,学生对象,学生对象] ——> [字典,字典,字典]
s1 = Student('德桦', '男', 81, '111', '刻骨铭心')
s2 = Student('志奇', '男', 22, '222', '我不是紫琦')
s3 = Student('紫琦', '男', 66, '333', '有请志奇')
stu_list = [s1, s2, s3]

# 列表推导式
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)

# 需求3:把{'德桦', '男', 81, '111', '刻骨铭心'} ——> 学生对象

s6 = Student(**__dict__)  # ** ——> 字典 ==> 对象
