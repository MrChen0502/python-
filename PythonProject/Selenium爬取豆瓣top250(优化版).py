# 导入 Selenium 的核心 webdriver，它提供了所有与浏览器交互的 API
import time
from asyncio import wait

from selenium import webdriver

# 导入 Edge 浏览器的配置类 Options
# Options 对象用来设置浏览器启动时的各种参数，比如是否保持打开、是否无头模式等
from selenium.webdriver.edge.options import Options

# 导入 By 类，它提供了所有元素定位的策略（如 ID、CLASS_NAME、XPATH 等）
# 使用 By 而不是直接写字符串，可以让代码更规范，IDE 也能提供自动补全
from selenium.webdriver.common.by import By

# 导入 WebDriverWait 类，它是实现“显式等待”的核心
# 它会根据你设定的超时时间，反复检查某个条件是否成立
from selenium.webdriver.support.ui import WebDriverWait

# 导入 expected_conditions 并简写为 EC
# 它里面预置了很多等待条件，比如元素是否存在、是否可点击、是否可见等
from selenium.webdriver.support import expected_conditions as EC

import csv


# 设置
def setting(url):
    options = Options()
    # 保持打打开网页
    options.add_experimental_option("detach" , True)
    driver = webdriver.Edge(options=options)
    # url = "https://movie.douban.com/top250"
    driver.get(url)

    return driver

# 解析电影数据
def get_movie_info(urls,driver):
    driver.get(urls)
    wait = WebDriverWait(driver, 10)

    wait.until((
        EC.presence_of_all_elements_located((By.XPATH,"//span[@property='v:itemreviewed']"))
    ))

    # 名字
    movie_name = driver.find_element(By.XPATH , "//span[@property='v:itemreviewed']").text

    # 上映年份
    movie_years = driver.find_element(By.XPATH , "//*[@id='content']/h1/span[2]").text

    # top值
    movie_top = driver.find_element(By.XPATH , "//*[@id='content']/div[1]/span[1]").text

    # 导演
    movie_directors = driver.find_element(By.XPATH , "//*[@id='info']/span[1]/span[2]/a").text

    # 演员
    # movie_actors = driver.find_element(By.XPATH , "")

    # 类型（用 contains 定位更稳定）
    movie_tags = driver.find_element(By.XPATH, "//span[contains(text(), '类型:')]").text
    movie_tags = movie_tags.split(':', 1)[1].strip() if ':' in movie_tags else movie_tags

    # 制片国家（修复 text()[n] 问题）
    try:
        country_elem = driver.find_element(By.XPATH, "//span[contains(text(), '制片国家/地区:')]")
        movie_country = country_elem.text.split(':', 1)[1].strip()
    except:
        movie_country = "未知"

    # 语言（修复 text()[n] 问题）
    try:
        lang_elem = driver.find_element(By.XPATH, "//span[contains(text(), '语言:')]")
        movie_language = lang_elem.text.split(':', 1)[1].strip()
    except:
        movie_language = "未知"

    # 上映日期（用 contains 定位）
    try:
        date_elem = driver.find_element(By.XPATH, "//span[contains(text(), '上映日期:')]")
        movie_dates = date_elem.text.split(':', 1)[1].strip()
    except:
        movie_dates = "未知"

    # 片长（用 contains 定位）
    try:
        runtime_elem = driver.find_element(By.XPATH, "//span[contains(text(), '片长:')]")
        movie_cost_times = runtime_elem.text.split(':', 1)[1].strip()
    except:
        movie_cost_times = "未知"

    # 豆瓣评分
    movie_rating = driver.find_element(By.XPATH , "//*[@id='interest_sectl']/div[1]/div[2]/strong").text

    print(movie_name)
    movie = {
        "名字": movie_name,
        "上映年份": movie_years,
        "top值": movie_top,
        "导演": movie_directors,
        "类型": movie_tags,
        "制片国家": movie_country,
        "语言": movie_language,
        "上映日期": movie_dates,
        "片长": movie_cost_times,
        "豆瓣评分": movie_rating,
    }

    return  movie


# 保存数组all_movies为csv文件
def save_all_movies(all_movies):
    """将电影数据列表保存为 CSV 文件"""
    # 1. 定义CSV文件的表头（必须和字典的键完全一致）
    fieldnames = [
        "名字",
        "上映年份",
        "top值",
        "导演",
        "类型",
        "制片国家",
        "语言",
        "上映日期",
        "片长",
        "豆瓣评分"
    ]

    # 2. 打开文件，写入数据
    with open('douban_top250.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # 写入表头
        writer.writerows(all_movies)  # 写入所有数据行

    print(f"\n✅ 数据已保存到 douban_top250.csv，共 {len(all_movies)} 条记录")


def main():
    url = "https://movie.douban.com/top250"
    driver = setting(url)
    waits = WebDriverWait(driver, 10)

    # 等待列表加载
    movie_items = waits.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='item']"))
    )

    # 关键改进：先提取所有详情页链接
    detail_urls = []
    for item in movie_items:
        detail_url = item.find_element(By.XPATH, "./div/a").get_attribute("href")
        detail_urls.append(detail_url)

    all_movies = []

    # 遍历链接，获取详情页数据
    for detail_url in detail_urls:
        time.sleep(5)
        print(f"正在获取：{detail_url}")
        movie_data = get_movie_info(detail_url, driver)
        if movie_data:
            all_movies.append(movie_data)

    print(f"\n共爬取 {len(all_movies)} 部电影")

    # 调用保存函数
    save_all_movies(all_movies)

    driver.quit()


if __name__ == '__main__':
    main()

