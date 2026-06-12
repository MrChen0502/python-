import requests

# 定义url
targe_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求 获取数据
response =  requests.get(targe_url)

# 输出数据到控制台
print(response.text)