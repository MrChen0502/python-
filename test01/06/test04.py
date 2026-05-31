import array


dArray = array.array('d' , [8.88 , 7.77 , 6.66])
for d in dArray:
    print(d)
# 字符串和字符的区别
# mmm —— 字符串
# m —— 字符

print("------------")
# 不推荐'u' ，python3.16以后被移除
sArray = array.array('u' , ["a" , "b" , "c" , "d"])
for s in sArray:
    print(s)

