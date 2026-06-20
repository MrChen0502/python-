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

    # 元素定位-xpath
    # 完整路径（定位值比较长 但是100%准确）
    # 相对路径 （属性如果是随机的 可能定位不到）

    # 使用完整路径定位输入框
    a1.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/form/span[1]/input").send_keys("python XPATH定位")

    time.sleep(5)
    a1.quit()