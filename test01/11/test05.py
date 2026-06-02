class Student:
    ## 为了实例属性前面加上 __ 属性是私有的
    ## 私有属性只能在当前类中使用
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

## 封装 修改实例属性的值 改成 通过方法来实现
    def toString(self):
        print(self.__name,str(self.__age))

    def setName(self,name,age):
        self.__name = name
        self.__age = age

s1 = Student("mayikt" , 18)
s1.toString()
s1.setName("xixi",20000)
s1.toString()
