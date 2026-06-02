from os import name


class Student:  ##定义第一个学生类
    ## 属性
    ## 定义构造方法 __init__（第一个参数self 指定的对象实例）
    def __init__(self,name,address,age):
        self.name  = name
        self.address = address
        self.age = age

## 构造的第一个实例对象 余胜军的徒儿
stu1=Student(10,100,1000)
stu2=Student(2,2,2)
print(stu1.name,str(stu1.age),stu1.address)
print(stu2)