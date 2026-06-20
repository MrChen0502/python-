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

    # 元素定位-NAME
    # 1.通过name定位元素，一般比较准确。
    # 2.并不是所有网页或者元素 都有name值
    a1.find_element(By.NAME, "wd").send_keys("python NAME定位")

    time.sleep(5)
    a1.quit()