"""
该文件用于记录 学生类 学生的属性信息为：姓名 性别 年龄 手机号 描述信息
"""

# 1.定义学生类
class Student:
    # 2.定义方法 初始化属性信息
    def __init__(self, name , gender , age , phone , desc):
        """

        :param name: 学生姓名
        :param gender: 学生性别
        :param age: 学生年龄
        :param phone: 学生手机号
        :param desc: 描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        :return:
        """
        return f"{self.name} {self.gender} {self.age} {self.phone} {self.desc}"

if __name__ == '__main__':
    s = Student("1","2","3","4","5")
    print(s)