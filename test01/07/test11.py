print("欢迎您使用余胜军徒儿开发的计算器软件")
print("开发者:余胜军徒儿")
number1=input("请输入第一个数字")
number2=input("请输入第二个数字")
print("请按照以下序号完成操作")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")
print("其他数字默认为加法")
type=int(input("请输入序号: "))
def retNumeber(n1,n2,type):
    match type:
        case 1:
            return float(n1)+float(n2)
        case 2:
            return float(n1)+float(n2)
        case 3:
            return float(n1)*float(n2)
        case 4:
            return float(n1)/float(n2)
        case _:
            return float(n1)+float(n2)

result = retNumeber(number1,number2,type)
print(f"计算结果为:{result}")