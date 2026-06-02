class Student:
    ## 属于类属性 每个实例都是共享的属性
    scholl = "余胜军IT培训学校"
    ## 构造方法 在我们类中不允许定义多个 否则报错
    ## 构造方法中参数列表的变量名称 == None 允许默认值 不用传递参数
    def __init__(self,name=None,age=None,address=None,imgUrl=None):
        ## 创建对象的时候 传递参数赋值
        self.name = name
        self.age = age
        self.address = address
        self.imgUrl = imgUrl
        ## 实例方法
    def getName(self):
        print(self.name)

    @classmethod
    def setSchool(stu,newSchool):
        stu.scholl = newSchool

    ## 类方法
    @classmethod
    def getSchool(self):
        print(self.scholl)

s1 = Student("mayikt")
s2 = Student("meite")
s1.getName()
s2.getName()

## 类方法的操作如下：
Student.setSchool("中国余胜军IT培训学校")
Student.getSchool()


