"""
案例：演示编解码

细节：
    1.编码 = 把我们看得懂的 转成 我们看不懂的
        '字符串'.encode(码表)
    2.解码 = 把我们看不懂的 转成 我们看得懂的
        二进制.decode(码表)
    3.只要乱码了 原因只有1个 编解码不同
    4.英文字母 数字 特殊符号无论什么码表都只占1个字节 中文在gbk占2个字节 utf-8中占3个字节
    5.二进制数据特殊写法 即：b'字母 数字 特殊符号'  该方式针对于中文无效
"""

# 需求1:编码
s1 = '黑马123abCD!@#'

print(s1.encode())          #b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(s1.encode('utf-8'))   #b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(s1.encode('gbk'))     #b'\xba\xda\xc2\xed123abCD!@#'

print('-' * 30)

# 需求2：解码
bys = b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'

s2 = bys.decode()
s3 = bys.decode('utf-8')
print(s2)
print(s3)
print('-' * 30)

s4 = bys.decode('gbk')
print(s4)   # 榛戦┈123abCD!@#