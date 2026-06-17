# 导包
import time
import random
import time
import requests
import csv
from lxml import html

# 网址
SCRAPE_URL = "https://quotes.toscrape.com/"


# 伪装请求头 防止封IP不让访问
# # 设置伪装请求头（模拟真实浏览器）
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
    "Referer": "https://quotes.toscrape.com"
}


# 主函数
def main():
    # 定义一个数组 存放数据
    all_Scrape = []
    # 发送请求
    response = requests.get(SCRAPE_URL , headers=headers , timeout=60)
    # 使用随机函数 模拟人类行为(1-5秒随机停留)
    time.sleep(random.randint(1,5))

    # 解析数据 获取名言
    document = html.fromstring(response.content)
    print(document)
    pass


if __name__ == '__main__':
    main()