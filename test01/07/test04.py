userName="mayikt"
## 获取字符串长度 len() 传递一个字符串 自动帮你计算出 字符串长度
print(len(userName))
## 指定一个字符串 获取首字母+"66"
userName1="mayikt"
userName2="yushengjun"
# print(userName1[0]+"66")
# print(userName2[0]+"66")

## 方法返回值和没有返回值
# 根据传递参数name的值 获取到首字母+66 返回结果
def uName(name):
    print(f"uName，获取传递参数name值:{name}")
    return name[0]+"66"
## def 定义方法函数 方法的名称 函数名称（参数列表名称）

## 先定义方法函数 再调用方法 方法的名称（参数的值）
ret1=uName(userName1)
ret2=uName(userName2)

print(f"ret1:{ret1}")
print(f"ret2:{ret2}")