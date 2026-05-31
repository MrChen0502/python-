import array
iArray = array.array('i' , [1,2,1,2,1,2,3,4,5,6])
index=iArray.index(2) ##查找该元素在数组中首次出现的位置
index1=iArray.count(6) ##统计元素出现次数
print(index)
print(index1)
arrayList = iArray.tolist()