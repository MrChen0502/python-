import requests
import csv
from lxml import html
from urllib3.filepost import writer

# 常量(在python中，一般定义为全部字母大写)
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
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
    # 1.发送请求 获取电影详情数据
    movie_response = requests.get(movie_info_url , timeout=60)
    print(f"发送请求{movie_info_url} 获取电影详情数据......")

    # 2.解析数据 获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")

    # 电影年份
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")

    # 上映时间
    movie_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")

    # 类型
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")

    # 时长
    movie_cost_times = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")

    # 评分
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")

    # 语言
    movie_language = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")

    # 导演
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")

    # 作者
    movie_author = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")

    # 主演
    # movie_lead_actor = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span")

    # Slogan
    movie_slogan = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")

    # 简介
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # print(movie_name)
    # print(movie_years)
    # print(movie_dates)
    # print(movie_tags)
    # print(movie_cost_times)
    # print(movie_scores)
    # print(movie_language)
    # print(movie_directors)
    # print(movie_author)
    # print(movie_slogan)
    # print(movie_descriptions)

    # print("="*1000)

    # 3.返回电影详情
    movie_info = {
        "电影名" : movie_name[0].strip() if movie_name else '',
        "年份" : movie_years[0].strip() if movie_years else '',
        "上映时间" : movie_dates[0].strip() if movie_dates else '',
        "类型" : ",".join(movie_tags) if movie_tags else '',
        "电影时长" : movie_cost_times[0].strip() if movie_cost_times else '',
        "评分" : movie_scores[0].strip() if movie_scores else '',
        "语言" : movie_language[0].strip() if movie_language else '',
        "导演" : ",".join(movie_directors).strip() if movie_directors else '',
        "作者" : ",".join(movie_author).strip() if movie_author else '',
        # 主演没写 待完善
        "宣传语" : movie_slogan[0].strip() if movie_slogan else '',
        "简介" : movie_descriptions[0].strip() if movie_descriptions else '',
    }
    # print(movie_info)
    return movie_info

# 保存电影数据 保存为csv文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE , "w" , encoding="utf-8" , newline="")as csvfile:
        writer =  csv.DictWriter(csvfile , fieldnames=["电影名","年份","上映时间","类型","电影时长","评分","语言","导演","作者","宣传语","简介"])
        writer.writeheader()            # 写入表头
        writer.writerows(all_movies)    # 写入数据



# 主函数 定义核心逻辑
def main():
    # 1.发送请求 获取高分电影榜单数据
    # , headers = HEADERS
    response =  requests.get(TMDB_TOP_URL , timeout=60)
    print("发送请求 获取TMDB电影榜单数据")

    # 2.解析数据 获取电影列表
    document =  html.fromstring(response.text)
    movie_list = document.xpath("/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
    # print(movie_list)
    # 3.遍历电影列表 获取电影详情
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            # 电影详情的url
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            # print(movie_info_url)
            # 发送请求 获取电影详情数据
            movie_info = get_movie_info(movie_info_url)
            all_movies.append(movie_info)

    # 4.保存数据 保存为csv文件
    print("获取到所有的电影详情 保存到电影数据到CSV文件")
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()