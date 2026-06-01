###用户登录注册
###1.容器 数据存储（集合存放在内存中、file文件、mysql数据库）
###2.用户名（不允许重复的）和用户密码
## 主菜单、注册、登录
userDic={}  ###键值对
##字典存放用户数据 key{用户名称}:value{用户密码}
while True:
    print("欢迎您进入余胜军IT教学网站")
    print("请输入序号操作")
    print("1.新用户注册")
    print("2.用户登录")
    print("0.退出")
    number=int(input("请输入序号完成操作： "))
    match number:
        case 1:
            while True:
                print("开始新用户注册：")
                userName=input("请输入新用户名称：")
                if userName in userDic:
                    print(f"该用户:{userName}已经存在,无法重复注册")
                else:
                    print(f"您输入的新用户名称为：{userName}")
                    userPwd=input("请输入新用户密码：")
                    print(f"您输入的新用户密码为：{userPwd}")
                    # 数据存储
                    userDic.update({ userName:userPwd})
                    print("恭喜您用户注册成功！")
                    break ##注册成功后退出循环
                print(userDic)
        case 2:
            ### 判断规则 ：根据用户输入的名称查找 key
            ### 在比较key对应的密码 如果是一致的情况下
            ## 则账号和密码验证成功
            userName=input("请输入用户名称")
            if userName in userDic:
                print("用户名称验证成功")
                ##验证密码
                userPwd = input("请输入密码")
                if userPwd == userDic[userName]:
                    print("密码验证成功")
                    print(f"已登录，欢迎您：{userName}")
                else:
                    print("密码错误")
            else:
                print("用户名称不存在")
                break
        case 0:
            print("已退出")
            break

