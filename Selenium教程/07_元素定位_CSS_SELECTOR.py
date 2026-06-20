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

    # 元素定位-CSS_SELECTOR
    # 1.#id = 井号+id值 通过id定位
    # 2. .class = 点 + class值 通过class定位
    # 3. 不加修饰符 = 标签头
    # 4.1 通过任意类型定位: "[类型='精准值']"
    # 4.2 通过任意类型定位: "[类型*='模糊值']"
    # 4.3 通过任意类型定位: "[类型^='开头值']"
    # 4.4 通过任意类型定位: "[类型$='结尾值']"

    # 使用CSS_SELECTOR定位输入框并输入内容
    # 方法1：通过id定位
    # a1.find_element(By.CSS_SELECTOR, "#kw").send_keys("python CSS_ID定位")

    # 方法2：通过class定位
    # a1.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys("python CSS_CLASS定位")

    # 方法3：通过属性定位
    a1.find_element(By.CSS_SELECTOR, "[name='wd']").send_keys("python CSS属性定位")

    time.sleep(5)
    a1.quit()