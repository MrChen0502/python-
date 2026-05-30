## 需求 给一个数值类型 判断是否是奇数或者偶数
num = input("请您输入一个数：")
newNum = int(num)
if newNum % 2==0:
    print(f"您输入的数字是偶数{num}")
else:
    print(f"您输入的数字是奇数{num}")