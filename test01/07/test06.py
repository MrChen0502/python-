## 有多个返回结果
def uName(name,age):
    return name+str(age),"meite","yushengjun"
u1,u2,u3=uName("mayikt",20)
print(u1)
print(u2)
print(u3)

## 该方法是没有返回结果
def uVodiName(name):
    print(name)
print(uVodiName("666"))