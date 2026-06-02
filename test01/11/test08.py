class Parent:
    def pk(self):
        print("Parent pk")

class Son1(Parent):
    def pk(self):
        super().pk()
        print("Son1 pk")

class Son2(Parent):
    def pk(self):
        print("Son2 pk")

## 多态 子类与父类中 方法的名称和参数列表相同 则直接重写 执行子方法
s1 = Son1()
s1.pk()
s2 = Son2()
s2.pk()
## 设计模式
## 对接支付 支付 父类 n多个子类 具体实现 支付宝 银联支付