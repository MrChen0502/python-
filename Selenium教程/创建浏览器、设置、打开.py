# 1. 禁用沙盒（一般不需要，除非在服务器跑）
# options.add_argument('--no-sandbox')
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options          # 用于设置 Edge 配置
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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

a1 = she("https://www.baidu.com")
print(a1.title)
# a1.get("https://www.baidu.com")

# 关闭标签页
# time.sleep(2)
# a1.close()

# 退出浏览器(关闭所有标签页)
# a1.quit()

# 浏览器最大化
time.sleep(2)
a1.maximize_window()    # 最大化
time.sleep(2)
a1.minimize_window()    # 最小化

