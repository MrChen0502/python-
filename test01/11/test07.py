### 多重继承示例

class A:
    def a(self):
        print("a")

class B:
    def b(self):
        print("b")

class C(A,B):
    def c(self):
        print("c")

c = C()
c.a()
c.b()