#用for循环输出三次登录机会
for i in range(3):
    userName=input("请输入账号：")
    print(f"您输入的账号为：{userName}")
    userPassword=input("请输入密码：")
    print(f"您输入的密码为：{userPassword}")

    if userName == "admin" and userPassword == "admin":
        print(f"登录成功！！欢迎您！{userName}先生/女士")
        break
    else:
        print(f"当前登录失败次数为{i+1},您还可以登录{2-i}次！！！")
        print("登录失败，请重试！！！")