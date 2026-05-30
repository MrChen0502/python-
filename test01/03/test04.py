count = 1
while count <= 3:
    print(f"开始第{count}次登录")
    userName=input("请输入账号： ")
    print(f"您输入的账号为：{userName}")
    userPassword=input("请输入密码： ")
    print(f"您输入的密码为{userPassword}")
    count += 1
    if userName == "admin" and userPassword == "admin":
        print("登录成功")
        break
    else:
        print("---")
        print("账号密码错误")