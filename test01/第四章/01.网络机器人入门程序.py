import requests
from lxml import html

# 定义url
targe_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求 获取数据
response =  requests.get(targe_url)

# 输出数据到控制台
# print(response.text)
document = html.fromstring(response.text)

# 解析数据
# 解析表头
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格数据
td_list = document.xpath("//tbody/tr")
for td in td_list:
    tds_list = td.xpath("./td/text()")
    print(tds_list)