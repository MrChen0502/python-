# 导入requests库 需要安装
import random
import time

import requests

# 导入csv库
import csv

# 导入lxml库 需要安装
from lxml import html

# 设置常量
DOUBAN_BASE_URL = "https://movie.douban.com"         # 需要抓取的网站链接(豆瓣)
DOUBAN_TOP_URL_1 = "https://movie.douban.com/top250" # 高分电影榜单的url(第一页)

# 伪装请求头 防止封IP不让访问
# # 设置伪装请求头（模拟真实浏览器）
# 更强的伪装请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "identity",
    "Referer": "https://www.douban.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Ch-UA": '"Not A(Brand";v="99", "Google Chrome";v="134", "Chromium";v="134"',
    "Sec-Ch-UA-Mobile": "?0",
    "Sec-Ch-UA-Platform": '"Windows"',
}

def get_movie_info(movie_info_url):
    pass


def save_all_movies(all_movies):
    pass

# 主函数 定义核心逻辑
def main():
    # 定义一个数组 存储获取到的电影数据
    all_movies = []
    # 发送请求
    response = requests.get(DOUBAN_TOP_URL_1 , headers=HEADERS , timeout=60)
    # 使用随机等待1-3秒 模拟人类浏览器
    time.sleep(random.randint(1,3))

    # 2.解析数据 获取电影列表
    document = html.fromstring(response.content)

    movie_list = document.xpath("//div[@class='item']")
    print(movie_list)

    for movie in movie_list:
        movie_url = movie.xpath("./div[@class='pic']/a/@href")
        if movie_url:
            movie_info_url = DOUBAN_BASE_URL + movie_url[0]
            print("返回的地址为：",movie_info_url)

            # 构造函数get_movie_info() 获取电影数据
            movie_info = get_movie_info(movie_info_url)

            # 保存电影数据到csv文件all_movies
            all_movies.append(movie_info)

    # 4.保存数据 保存为csv文件
    # 创建save_all_movies()函数，保存为cvs文件
    print("保存ing...")
    save_all_movies(all_movies)

    # print(f"状态码: {response.status_code}")
    # print(f"内容长度: {len(response.text)}")
    # print(f"编码: {response.encoding}")
    # print("前200字符:")
    # print(response.text[:200])

if __name__ == '__main__':
    main()