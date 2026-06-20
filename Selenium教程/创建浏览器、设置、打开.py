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
    a1 = she("https://www.baidu.com/")
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
    # a2 = a1.find_element(By.ID, "kw")

    # 元素定位-NAME
    # 1.通过name定位元素，一般比较准确。
    # 2.并不是所有网页或者元素 都有name值
    # a1.find_element(By.NAME, "wd").send_keys("python")

    # 元素定位-CLASS_NAME
    # 1.class值不能有空格 否则报错
    # 2.class值重复的有很多 需要切片
    # a1.find_elements(By.CLASS_NAME, "channel-icons__item")[1].click()

    # 元素定位—TAG_NAME
    # 1.查找<开头标名字>
    # 2.重复的标签名字特别多，需要切片
    # a1.find_elements(By.TAG_NAME, "a")[0].click()
    # time.sleep(5)
    # # 退出浏览器(关闭所有标签页)
    # a1.quit()

    # 元素定位-LINK_TEXT
    # 通过精准链接文本找到a标签的元素
    # 用重复的文本 需要切片
    # a1.find_element(By.LINK_TEXT, "新闻").click()
    # # 退出浏览器(关闭所有标签页)
    # time.sleep(5)
    # a1.quit()

    # 元素定位-PARTIAL_LINK_TEXT
    # 通过模糊链接文本找到a标签的元素
    # 用重复的文本 需要切片
    # a1.find_element(By.PARTIAL_LINK_TEXT, "新闻").click()
    # # 退出浏览器(关闭所有标签页)
    # time.sleep(5)
    # a1.quit()

    # 元素定位-CSS_SELECTOR
    # 1.#id = 井号+id值 通过id定位
    # 2. .class = 点 + class值 通过class定位
    # 3. 不加修饰符 = 标签头
    # 4.1 通过任意类型定位: "[类型='精准值']"
    # 4.2 通过任意类型定位: "[类型*='模糊值']"
    # 4.3 通过任意类型定位: "[类型^='开头值']"
    # 4.4 通过任意类型定位: "[类型$='结尾值']"
    # 以上这些方法都属于理论定位法

    # 5.更简单的定位方式 在浏览器控制台直接复制相对应的SELECTOR
    # a1.find_elements(By.CSS_SELECTOR, "[autocomolete='off']")[7].send_keys("python")
    # # 退出浏览器(关闭所有标签页)
    # time.sleep(5)
    # a1.quit()

    # 元素定位-xpath
    # 完整路径（定位值比较长 但是100%准确）
    # 相对路径 （属性如果是随机的 可能定位不到）
    # a1.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/form/span[1]/input").click()
    # # 退出浏览器(关闭所有标签页)
    # time.sleep(5)
    # a1.quit()





    # # 定位多个元素(找到的话返回列表形式、找不到的话返回空列表)
    # a1.find_elements(By.ID, "kw")

    # 元素输入
    # a2.send_keys("python")
    # # 元素清空
    # time.sleep(2)
    # a2.clear()
    #
    # a2 = a1.find_element(By.ID, "su")

    # 元素点击
    # a2.click()


    # 元素定位隐性等待（多少秒内找到元素就立即执行，没找到就报错）
    a1.implicitly_wait(10)
    a1.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/form/span[1]/input").click()
    # 退出浏览器(关闭所有标签页)
    time.sleep(5)
    a1.quit()



    # 以下代码仅做演示 不做实际效果
    # 获取全部标签页句柄
    a2 = a1.window_handles

    a1.close()

    # 通过句柄切换标签页
    a1.switch_to.window(a2[1])
    # 获取当前标签页句柄
    a2 = a1.current_window_handle
    print(a2)



