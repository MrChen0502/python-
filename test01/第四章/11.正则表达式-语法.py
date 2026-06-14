import re

s1 = "18809090000是我的手机号，188开头的，以00结尾的；我的另一个手机号是15500008888，两个QQ号分别是1259989092和13809091293821，邮箱为python666@163.com，请给我发邮件。"


# 正则表达式
print(re.findall(r"188.*", s1)) # * 匹配任何个
print(re.findall(r"188.?", s1)) # ? 匹配0个或者1个（最多出现一次）
print(re.findall(r"188.+", s1)) # + 匹配1个或者多个（最少出现一次）

# print(re.findall(r"188\d{8}", s1))
# print(re.findall(r"155\d{6,10}", s1))
# print(re.findall(r"155\d{6,}", s1))

# print(re.findall(r"1[38]\d{8}", s1))
# print(re.findall(r"1[^38]\d{8}", s1))
# print(re.findall(r"1[3-9]\d{8}", s1))
# print(re.findall(r"^1[3-9]\d{9}", s1))
# print(re.findall(r"^1[3-9]\d{9}$", s1))

# print(re.findall(r"\w+@\w+\.\w+", s1))