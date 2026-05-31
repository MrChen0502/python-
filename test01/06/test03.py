import array ###引入python中数组的库
# 创建一个数组(定义一个数组类型 i 整数类型 ) 每个元素存放整数类型
# 每个元素必须是同一个数组类型
mayiktArray = array.array('i',[1,2,3,4,5])
print(mayiktArray[0])
print("------------")
for m in mayiktArray:
    print(m)        ##类似java中泛型