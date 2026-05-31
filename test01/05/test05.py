mayiktArray=["mayikt01" , "meite" , "wangmazi" , "yushengjun"]
print("数组中的数据未修改之前:")
for m in mayiktArray:
    print(m)
print("--------------------")
print("数组中的数据发生改变：")
# 修改数组中数据
mayiktArray[1] = "mayikt"
mayiktArray[3] = "yushengjun644"
for m in mayiktArray:
    print(m)
# 查询数据
# print(mayiktArray[3])
# # 追加数据
# mayiktArray.append("new01")
# for index in range(0,arrAyLen):
#     print(f"index:{index}，数据：{mayiktArray[index]}")

# 删除元素
mayiktArray.remove("wangmazi")

del mayiktArray[0]

mayiktArray.clear() ## 清空数据

# 获取数组长度
arrAyLen = len(mayiktArray)

for m in range(0,arrAyLen):
    print(f"m:{m},数据：{mayiktArray[m]}")