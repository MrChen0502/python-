mayiktStudentArray = [] ##定义一个空的数组容器 来进行存放数据
while True:
    print("欢迎您进入学生管理系统")
    print("开发者：余胜军的徒儿")
    print("1.查询所有学生信息")
    print("2.增加新的学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.查找学生信息是否存在")

    # 需要将用户输入的数据转换int类型
    num = int(input("请输入以上需要选择:"))
    mayiktStudentArrayLen = len(mayiktStudentArray)
    match num:
        case 1: ##查询所有学生信息
            for index in range(mayiktStudentArrayLen):
                print(f"index:{index},数据：{mayiktStudentArray[index]}")
        case 2: ##增加新的学生信息
            newStuName = input("请输入新增学生信息名称")
            mayiktStudentArray.append(newStuName)
            print(f"学生{newStuName}新增成功")
        case 3: ##删除学生信息
            stuIndex = input("请输入需要删除学生的名字：")
            flag = False
            for index in range(mayiktStudentArrayLen):
                userIndex = mayiktStudentArray[index]
                if stuIndex == userIndex:
                    print(f"该学生信息是:{stuIndex}")
                    flag = True
                    break
            if flag:
                mayiktStudentArray.remove(stuIndex)
                print(f"已成功删除学生信息{stuIndex}")
            else:
                print("该学生信息不存在，请确认无误后再删除！！！")
        case 4: ##修改学生信息
            userstuName = input("请输入查找学生的名称")
            flag = False  ## 标记数组中是否查找到该元素 查找到返回True 否则False
            for index in range(mayiktStudentArrayLen):
                stuName = mayiktStudentArray[index]
                if userstuName == stuName:
                    flag = True
                    print(f"该学生{userstuName}存在")
                    userName =  input("请输入修改学生信息名称")
                    mayiktStudentArray[index] = userName
                    print(f"该学生原名称为：{userstuName}，已更改成{userName}")
                    break
                if flag == False:
                    print("学生不存在，修改名称失败")
                    mayiktStudentArray.append(userstuName)
        case 5: ##根据学生名称 查找学生是否存在
            userstuName=input("请输入查找学生的名称")
            flag = False ## 标记数组中是否查找到该元素 查找到返回True 否则False
            for index in range(mayiktStudentArrayLen):
                stuName = mayiktStudentArray[index]
                if userstuName == stuName:
                    flag = True
                    break
                # 应该在for循环外面
            if flag:
                print(f"该学生{userstuName}存在")
            else:
                print(f"该学生{userstuName}不存在")

    print("------------------------------------------------------------")
