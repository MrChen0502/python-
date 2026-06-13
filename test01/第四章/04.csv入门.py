# csv操作 - 方式一:文件操作的原始方式
# 写
from urllib3.filepost import writer
#
# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")    # 写入表格
#     f.write("小王,18,男,football\n")   #写入表格
#     f.write("小李,18,女,Python\n")
#     f.write("小张,18,男,C++\n")
#     f.write("小王,20,男,Go\n")
#
# # 读取
# with open("csv_data/01.csv", "r",encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())

# csv操作 - 方式二：csv
import csv

with open("csv_data/02.csv","w",encoding="utf-8",newline="")as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()    # 写入表头
    writer.writerow({"姓名": "小王", "年龄": 18, "性别": "男", "爱好": "Python"})    # 写入数据
    writer.writerow({"姓名": "小李", "年龄": 19, "性别": "女", "爱好": "篮球"})
    writer.writerow({"姓名": "小张", "年龄": 20, "性别": "男", "爱好": "C++"})
    writer.writerow({"姓名": "小赵", "年龄": 21, "性别": "女", "爱好": "跳舞"})
    writer.writerow({"姓名": "小孙", "年龄": 22, "性别": "男", "爱好": "吉他"})
    writer.writerow({"姓名": "小周", "年龄": 23, "性别": "女", "爱好": "阅读"})

# 读取
with open("csv_data/02.csv","r",encoding="utf-8")as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)