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
    def show_view(self):
        print('*' * 23)
        print("学生管理系统")
        print("\t1.添加学生信息")
        print("\t2.修改学生信息")
        print("\t3.删除学员")
        print("\t4.查询学生信息（单一）")
        print("\t5.显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.添加学生信息")
        print('*' * 23)
        print()

    # 4.定义函数，实现添加学生信息功能
    def add_student(self):
        pass

    # 5.删除学员
    def del_student(self):
        pass

    # 6.修改
    def update_student(self):
        pass

    # 7.查询学生信息（单一）
    def search_one_student(self):
        pass

    # 8.查询所有
    def search__all_student(self):
        pass

    # 9.保存学生信息
    def save_student(self):
        pass

    # 10.加载学生信息系统
    def load_student(self):
        pass

    # 11.定义函数 把上述所有业务逻辑跑通
    def start(self):
        # 11.1
        # 11.2 死循环 不断
        while True:
            # 11.3
            # 11.4 打印提示界面
            self.show_view()
            # 11.5 提示用户录入要操作的编号 并接收
            input_num = input("请输入您要操作的编号： ")
            # 11.6 根据用户输入的编号 做不同的操作
            if input_num == "1":
                # 添加学生信息
                print("添加学生信息 \n")
                self.add_student()
            elif input_num == "2":
                # 删除学生信息
                print("删除学生信息 \n")
                self.del_student()
            elif input_num == "3":
                # 修改学生信息
                print("修改学生信息\n")
                self.update_student()
            elif input_num == "4":
                # 查询单个学生信息
                print("查询单个学生信息\n")
                self.search_one_student()
            elif input_num == "5":
                # 查询所有学生信息
                print("查询所有学生信息\n")
                self.search__all_student()
            elif input_num == "6":
                # 保存学生信息
                print("保存学生信息\n")
                self.save_student()
            elif input_num == "0":
                # 退出系统 二次校验
                print("退出系统\n")
                result = input("您确定要退出吗 (Y/N) ——> \n")
                if result.lower()  == "Y":  # 字符串的lower()  ——> 把字母转换成小写形式
                    print("谢谢您的使用 期待下次再会！")
                    break
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