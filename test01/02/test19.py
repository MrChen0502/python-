## 需求： 使用input 接收用户输入的 账号密码 判断 账号密码都必须为admin

username = input("请输入账号：")
userpassword = input("请输入密码：")

if username == "admin" and userpassword == "admin":
    print("登录成功")
else:
    print("账号密码错误，请重试")