import requests
import csv
from lxml import html

# 常量(在python中，一般定义为全部字母大写)
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

# # 设置伪装请求头（模拟真实浏览器）
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://www.themoviedb.org/"
# }

# 获取电影详情
def get_movie_info(movie_info_url):
    pass

# 保存电影数据 保存为csv文件
def save_all_movies(all_movies):
    pass


# 主函数 定义核心逻辑
def main():
    # 1.发送请求 获取高分电影榜单数据
    # , headers = HEADERS
    response =  requests.get(TMDB_TOP_URL , timeout=60)

    # 2.解析数据 获取电影列表
    document =  html.fromstring(response.text)
    movie_list = document.xpath("/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
    print(movie_list)
    # 3.遍历电影列表 获取电影详情
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/div/img/@src")
        if movie_urls:
            # 电影详情的url
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            # 发送请求 获取电影详情数据
            movie_info = get_movie_info(movie_info_url)

    # 4.保存数据 保存为csv文件
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()