class Parent: ## 定义父类
    parentName = "我是父类的名称：mayikt"
    def parent(self):
        print("我是父类中的parent 方法")

    @classmethod
    def setParentName(self,name):
        self.parentName = name
## 定义了子类 继承 Parent父类 属性 方法 继承过来
class Son1(Parent):
    def son(self):
        super().parent() ### super()函数调用父类方法
        super().setParentName("ahahahahahahahahahahahahahah")
        print(self.parentName)

        print("我是子类中的方法son()")

s1 = Son1()
s1.son()