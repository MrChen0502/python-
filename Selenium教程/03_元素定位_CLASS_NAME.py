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

    # 元素定位-CLASS_NAME
    # 1.class值不能有空格 否则报错
    # 2.class值重复的有很多 需要切片
    # 百度首页用class定位输入框（注意：s_ipt是输入框的class）
    a1.find_element(By.CLASS_NAME, "s_ipt").send_keys("python CLASS_NAME定位")

    time.sleep(5)
    a1.quit()