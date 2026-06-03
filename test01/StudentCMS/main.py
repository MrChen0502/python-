"""
该文件 用于程序的入口文件
"""

# 导包
from studentCMS import  StudentCMS

# 程序的主入口
if __name__ == '__main__':
    # 1.创建学生管理系统对象
    stu_cms = StudentCMS()
    # 2.启动程序
    stu_cms.start()