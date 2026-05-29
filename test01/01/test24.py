#str(将数据类型转化字符串)
# int（将数据类型转换int）
# float（将数据类型转化为浮点数）
# bool（将数据类型转化为bool）
str1="666"
a=10
b=5
# 求和：需要转换成同一类型
c=a+b+float(str1)
print(c)

f=66.12345
print(f)
# 浮点数数据转换为int类型会丢失精度
d=int(f)
print(d)