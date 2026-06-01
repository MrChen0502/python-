### python 字典 类似json 类似 java中map集合 键值对集合 key(唯一) value
### key 不允许重复
dac={"userName":"mayikt","userPwd":"123456","img":["img01","img02"]}

# 新增
dac.update({"address":"湖北武汉"})

print(dac)
print(dac["img"][1])
# 遍历键值对
for key in dac.keys():
    print(f"key:{key},value:{dac[key]}")