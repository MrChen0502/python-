import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


def she(url):
    q1 = Options()
    q1.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=q1)
    driver.get(url)
    return driver


if __name__ == '__main__':
    a1 = she("https://www.baidu.com/")
    print(a1.title)

    # 元素定位—TAG_NAME
    # 1.查找<开头标名字>
    # 2.重复的标签名字特别多，需要切片
    # 通过标签名定位a标签，点击第8个链接（新闻）
    a1.find_elements(By.TAG_NAME, "a")[7].click()

    time.sleep(5)
    a1.quit()