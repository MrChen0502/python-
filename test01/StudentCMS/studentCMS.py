"""
该文件用于 完成学生管理系统的 具体业务的操作 即：增删改查，保存学生信息...
"""
import time

# 导包
from student import Student

# 1.创建学生管理系统类
class StudentCMS(object):
    # 2.通过方法init，初始化属性信息
    def __init__(self):
        # 创建一个空列表篇 用于存储学生信息
        self.stu_list = []      # [学生对象，学生对象，学生对象] ——>[Student(...)]

    # 3.定义函数，实现打印 管理系统的页面
    # 因为该函数中没有使用self 所以可以把该函数定义为静态方法
    @staticmethod
    def show_view(self):
        print('*' * 23)
        print("学生管理系统")
        print("\t1.添加学生信息")
        print("\t2.删除学员")
        print("\t3.修改学生信息")
        print("\t4.查询学生信息（单一）")
        print("\t5.显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print('*' * 23)
        print()

    # 4.定义函数，实现添加学生信息功能
    def add_student(self):
        # 4.1 提示用户输入学生信息 并接收
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        age = str(input("请输入学生年龄："))  # 可能是整数，需要转换类型
        phone = input("请输入学生手机号：")
        desc = input("请输入学生描述信息：")
        # 4.2 把上述信息封装成学生对象
        stu = Student(name, gender, age, phone, desc)
        # 4.2 把学生对象添加到列表中
        self.stu_list.append(stu)
        # 4.4 提示
        print(f"添加{name}学生信息成功！！ \n")


    # 5.删除学员
    def del_student(self):
        # 5.1 提示用户输入要删除的学生姓名 并接收
        del_name = input("请输入需要删除的学生姓名")
        # 5.2 遍历列表 找到要删除的学生 并删除
        for stu in self.stu_list:  # stu在这里代之需要删除的学生对象
            if del_name == stu.name:
                self.stu_list.remove(stu)  # 已成功删除
                print(f"学生 {del_name} 信息删除成功 \n")
                break
        else:
            # else 说明没有break 即：没有找到该学生
            print("查无此人 请检查后重新删除! \n")

    # 6.修改
    def update_student(self):
        # 6.1 提示用户输入要修改的学生姓名 并接收
        upd_name = input("请输入需要删除的学生姓名")
        # 6.2 遍历列表 找到要修改的学生 并删除
        for stu in self.stu_list:  # stu在这里代之需要修改的学生对象
            # 6.3 如果当前学生的姓名 和 要修改的学生相同 就修改该学生信息
            if upd_name == stu.name:
                # 6.4 提示用户录入该学员新的信息
                stu.gender = int(input("请录入修改后的性别："))
                stu.age = int(input("请录入修改后的年龄："))
                stu.phone = int(input("请录入修改后的手机号："))
                stu.desc = int(input("请录入修改后的详细信息："))

                self.stu_list.remove(stu)  # 已成功修改
                print(f"学生 {upd_name} 信息修改成功 \n")
                break
        else:
            # else 说明没有break 即：没有找到该学生
            print("查无此人 请检查后重新修改! \n")

    # 7.查询学生信息（单一）
    def search_one_student(self):
        # 7.1 提示用户输入要修改的学生姓名 并接收
        search_name = input("请输入需要查找的学生姓名")
        # 7.2 遍历列表 找到要修改的学生 并查找
        for stu in self.stu_list:  # stu在这里代之需要修改的学生对象
            # 7.3 如果当前学生的姓名 和 要查找的学生相同 就查找该学生信息
            if search_name == stu.name:
                print(stu , end="\n")
                break
        else:
            # else 说明没有break 即：没有找到该学生
            print("查无此人 请检查后重新操作! \n")

    # 8.查询所有
    def search__all_student(self):
        # 8.1 判断列表长度是否为0 如果为0 提示：暂无学生信息 请添加后查询
        if len(self.stu_list) == 0:
            print("暂无学生信息 请添加后查询！\n")
        else:
            # 8.2 如果长度不为0 遍历列表 打印出所有的学生信息
            for i in self.stu_list:
                print(i)
            print()

    # 9.保存学生信息
    def save_student(self):
        # 9.1 关联 学生信息文件
        with open('./stu_data.txt' , 'w' , encoding='utf-8') as dest_f:
            # 9.2 把[学生对象，学生对象，学生对象......] ——> [字典,字典,字典......]
            stu_dict = [ stu.__dict__ for stu in self.stu_list]
            # 9.3 把字典列表 持久化到文件中
            dest_f.write(str(stu_dict)) # 转换成字符串再写入

    # 10.加载学生信息系统
    def load_student(self):
        """加载学生信息"""
        import os

        # 检查文件是否存在且不为空
        if not os.path.exists('./stu_data.txt'):
            print("首次启动，未找到存档文件...")
            return

        # 检查文件是否为空
        if os.path.getsize('./stu_data.txt') == 0:
            print("存档文件为空，请先添加学生信息并保存...")
            return

        try:
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f:
                stu_data = src_f.read()

                # 确保读取的内容不为空
                if stu_data:
                    stu_list = eval(stu_data)
                    # 把读取的字典列表转换成 Student 对象列表
                    self.stu_list = []
                    for stu_dict in stu_list:
                        stu = Student(
                            stu_dict['name'],
                            stu_dict['gender'],
                            stu_dict['age'],
                            stu_dict['phone'],
                            stu_dict['desc']
                        )
                        self.stu_list.append(stu)
                    print(f"成功加载 {len(self.stu_list)} 条学生信息")
                else:
                    print("没有找到学生信息")

        except FileNotFoundError:
            print("存档文件不存在，首次使用系统")
        except Exception as e:
            print(f"加载失败：{e}")


    # 11.定义函数 把上述所有业务逻辑跑通
    def start(self):
        # 11.1 加载学生信息
        self.load_student()
        # 11.2 死循环 不断
        while True:
            # 11.3 为了效果更明显 加入延迟
            time.sleep(1)
            # 11.4 打印提示界面
            StudentCMS.show_view()
            # 11.5 提示用户录入要操作的编号 并接收 
            input_num = input("请输入您要操作的编号： ")
            # 11.6 根据用户输入的编号 做不同的操作
            if input_num == "1":
                # 添加学生信息
                # print("添加学生信息 \n")
                self.add_student()
            elif input_num == "2":
                # 删除学生信息
                # print("删除学生信息 \n")
                self.del_student()
            elif input_num == "3":
                # 修改学生信息
                # print("修改学生信息\n")
                self.update_student()
            elif input_num == "4":
                # 查询单个学生信息(单一)
                # print("查询单个学生信息\n")
                self.search_one_student()
            elif input_num == "5":
                # 查询所有学生信息
                # print("查询所有学生信息\n")
                self.search__all_student()
            elif input_num == "6":
                # 保存学生信息
                print("保存学生信息\n")
                self.save_student()
            elif input_num == "0":
                # 退出系统 二次校验
                print("退出系统\n")
                result = input("您确定要退出吗 (Y/N) ——> \n")
                if result.lower()  == "y":  # 字符串的lower()  ——> 把字母转换成小写形式
                    # 在退出前 自动保存学生数据到文件
                    self.save_student()
                    print("谢谢您的使用 期待下次再会！")
                    break
            else:
                # 输入错误
                print("输入错误,请重新输入！\n")

# 12.在main中测试
if __name__ == '__main__':
    # 12.1 创建学生管理系统对象
    cms = StudentCMS()
    # 12.2 调用学生管理系统对象的start()函数 启动学生管理系统
    cms.start()