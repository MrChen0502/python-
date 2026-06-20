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

    # 元素定位-PARTIAL_LINK_TEXT
    # 通过模糊链接文本找到a标签的元素
    # 用重复的文本 需要切片
    a1.find_element(By.PARTIAL_LINK_TEXT, "新").click()

    time.sleep(5)
    a1.quit()