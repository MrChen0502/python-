import time
import random
import requests
import csv
from lxml import html

# 网址
SCRAPE_URL = "https://quotes.toscrape.com/"

# 伪装请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
    "Referer": "https://quotes.toscrape.com"
}


# 保存文件
def save_all_scrape(all_Scrape):
    """将数据列表保存为CSV文件"""
    with open('csv_data/text01.csv', 'w', encoding='utf-8-sig', newline="") as csvfile:
        # 注意：这里的字段名必须和字典的键完全一致
        writer = csv.DictWriter(csvfile, fieldnames=["名言", "作者", "标签"])
        writer.writeheader()
        writer.writerows(all_Scrape)
    print(f"数据已保存，共 {len(all_Scrape)} 条")


# 主函数
def main():
    # 存放所有数据的列表，每个元素是一个字典
    all_Scrape = []
    for page_num in range(1,11):
        if page_num == 1:
            url = SCRAPE_URL
        else:
            url = f"https://quotes.toscrape.com/page/{page_num}"


        # 发送请求
        response = requests.get(url, headers=headers, timeout=60)
        # 模拟人类行为
        time.sleep(random.randint(1, 3))
        # 解析数据
        document = html.fromstring(response.content)

        # 找到所有名言卡片
        quote_divs = document.xpath("//div[@class='quote']")
        print(f"找到 {len(quote_divs)} 条名言\n" + "=" * 50)

        # 循环遍历每个名言卡片
        for quote_div in quote_divs:
            # 1. 提取名言文本
            text = quote_div.xpath(".//span[@class='text']/text()")
            text = text[0].strip() if text else "未知名言"

            # 2. 提取作者
            author = quote_div.xpath(".//small[@class='author']/text()")
            author = author[0].strip() if author else "未知作者"

            # 3. 提取所有标签
            tags = quote_div.xpath(".//a[@class='tag']/text()")
            tags_str = ', '.join(tag.strip() for tag in tags) if tags else "无标签"

            # 4. 将本条数据存为字典，并添加到总列表
            all_Scrape.append({
                "名言": text,
                "作者": author,
                "标签": tags_str
            })

            # 打印进度
            print(f"名言：{text}")
            print(f"作者：{author}")
            print(f"标签：{tags_str}")
            print("-" * 50)

        # 保存数据
        save_all_scrape(all_Scrape)


if __name__ == '__main__':
    main()