class Student:
    ## 属于类属性 每个实例都是共享的属性
    scholl = "余胜军IT学习"
    ## 构造方法 在我们类中不允许定义多个 否则报错
    ## 构造方法中参数列表的变量名称 == None 允许默认值 不用传递参数
    def __init__(self,name=None,age=None,address=None):
        ## 创建对象的时候 传递参数赋值
        self.name = name
        self.age = age
        self.address = address

## 不能跟封装的函数同级
stu1 = Student("xixi",18,"guangzhou")
stu2 = Student("xixi",age=10000)
print(stu1.name,stu1.age,stu1.address)
print(stu2.name,str(stu2.age))
## 实例属性与类属性区别
## 实例属性属于每个对象独立的属性
## 类型同同一个类中共享的属性