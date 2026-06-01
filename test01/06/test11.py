### python 字典 类似json 类似 java中map集合 键值对集合 key(唯一) value
### key 不允许重复
dac={"userName":"mayikt","userPwd":"123456"}
# 查询
print(dac)
# 修改
dac["userName"]="wangmazi"
print(dac["userName"])
print("-------------")
# 删除key
del dac["userPwd"]
print("userPwd" in dac)
if "userPwd" in dac:
    print(dac["userPwd"])
### key:value
## 查询根据key查找