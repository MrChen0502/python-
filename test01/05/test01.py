# 定义一个容器 存放很多的元素
mayiktArray=["mmm" , "mayikt" , "yushengjun" , True , 66 , 88]
### 数据访问是通过index 下标
print(mayiktArray[0])
print(mayiktArray[1])

# 获取数组长度 进行实时增加或删除
arrAyLen=len(mayiktArray)
print(f"数组的长度为{arrAyLen}")
# 如何遍历数组
# 动态长度
for i in range(0,arrAyLen):
    print(f"mayiktArray[{i}]=={mayiktArray[i]}")

# 方式2 迭代器
print("------------------------------")
for j in mayiktArray:
    print(j)