# 1. 禁用沙盒（一般不需要，除非在服务器跑）
# options.add_argument('--no-sandbox')
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options          # 用于设置 Edge 配置
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By         #元素定位导包

# 设置浏览器、启动浏览器
def she(url):
    # 创建设置浏览器对象
    q1 = Options()

    # 2. 保持浏览器打开（调试时很有用）
    q1.add_experimental_option('detach', True)

    # 3. 启动浏览器（用 Edge）
    driver = webdriver.Edge(options=q1)
    driver.get(url)
    # driver.get("https://www.douban.com") ==> driver = webdriver.Edge(service=Service('msedgedriver.exe'), options=q1)
    return driver


if __name__ == '__main__':
    a1 = she("https://www.baidu.com")
    print(a1.title)
    # a1.get("https://www.baidu.com")

    # 关闭标签页
    # time.sleep(2)
    # a1.close()

    # 退出浏览器(关闭所有标签页)
    # a1.quit()

    # 浏览器最大化
    # time.sleep(2)
    # a1.maximize_window()    # 最大化
    # time.sleep(2)
    # a1.minimize_window()    # 最小化


    # 浏览器打开位置、尺寸
    # a1.set_window_position(200,200)         #位置
    #
    # a1.set_window_size(1920,1080)    #尺寸

    # 浏览器截图
    # a1.get_screenshot_as_file('1.png')
    #
    # # 浏览器刷新当前网页
    # a1.refresh()

    # 定位一个元素(找到的话返回结果、找不到的话报错)
    # 元素定位-ID
    # 1.通过ID定位元素 一般般都比较准确
    # 2.并不是所有网页或者元素 都有ID值
    a2 = a1.find_element(By.ID, "kw")
    #
    # # 定位多个元素(找到的话返回列表形式、找不到的话返回空列表)
    # a1.find_elements(By.ID, "kw")

    # 元素输入
    a2.send_keys("python")
    # 元素清空
    time.sleep(2)
    a2.clear()

    a2 = a1.find_element(By.ID, "su")

    # 元素点击
    # a2.click()



