# 导入 time 模块，用于在代码中强制暂停（等待）
# 这里主要用于两个地方：1. 观察浏览器运行过程；2. 最终关闭浏览器前的留白
import time

# 导入 Selenium 的核心 webdriver，它提供了所有与浏览器交互的 API
from selenium import webdriver

# 导入 Edge 浏览器的配置类 Options
# Options 对象用来设置浏览器启动时的各种参数，比如是否保持打开、是否无头模式等
from selenium.webdriver.edge.options import Options

# 导入 By 类，它提供了所有元素定位的策略（如 ID、CLASS_NAME、XPATH 等）
# 使用 By 而不是直接写字符串，可以让代码更规范，IDE 也能提供自动补全
from selenium.webdriver.common.by import By

# 导入 WebDriverWait 类，它是实现“显式等待”的核心
# 它会根据你设定的超时时间，反复检查某个条件是否成立
from selenium.webdriver.support.ui import WebDriverWait

# 导入 expected_conditions 并简写为 EC
# 它里面预置了很多等待条件，比如元素是否存在、是否可点击、是否可见等
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# 第一步：创建浏览器配置对象
# ============================================================

# 实例化一个 Options 对象，用于存放 Edge 浏览器的启动配置
options = Options()

# 添加一个实验性配置项 'detach'，并设为 True
# 它的作用是：当 Python 代码执行完毕后，不自动关闭浏览器窗口
# 这样方便你观察页面状态，或者在调试时手动操作浏览器
options.add_experimental_option("detach", True)


# ============================================================
# 第二步：启动浏览器并访问目标网址
# ============================================================

# 根据配置（options）启动 Edge 浏览器，并返回一个 driver 对象
# driver 是 Selenium 的“遥控器”，所有后续操作（打开网址、找元素、点击等）都通过它完成
driver = webdriver.Edge(options=options)

# 通过 driver 的 get() 方法，让浏览器导航（跳转）到豆瓣 Top250 页面
driver.get("https://movie.douban.com/top250")


# ============================================================
# 第三步：设置显式等待
# ============================================================

# 创建一个 WebDriverWait 实例，命名为 waits
# 它绑定了 driver，并设置了最长等待时间为 10 秒
# 之后，用 waits.until() 去等待某个条件成立时，最多会等待 10 秒
waits = WebDriverWait(driver, 10)


# ============================================================
# 第四步：等待所有电影条目加载完成
# ============================================================

# 调用 waits.until() 方法，它接收一个条件作为参数
# EC.presence_of_all_elements_located(...) 是 expected_conditions 提供的一个条件
# 它的含义是：“等待页面上至少存在一个匹配定位器的元素，并返回所有匹配元素的列表”
# 参数 (By.XPATH, "//div[@class='item']") 是一个元组，指定了定位策略（XPath）和定位值
# 如果 10 秒内找到了至少一个元素，until() 会返回找到的元素列表（List[WebElement]）
# 如果 10 秒后仍然没找到，until() 会抛出 TimeoutException 异常
movies_item = waits.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='item']"))
)


# ============================================================
# 第五步：打印信息并准备存储数据
# ============================================================

# 使用 len() 获取列表长度，即找到了多少部电影，然后打印出来
print(f"找到 {len(movies_item)} 部电影\n" + "=" * 50)

# 初始化一个空列表 all_movies，用于在循环中存储每部电影的数据（以字典形式）
all_movies = []


# ============================================================
# 第六步：遍历每一部电影，提取详细信息
# ============================================================

# 使用 for 循环遍历 movies_item 列表，每次循环处理一部电影
# 这里的 movie 是一个 WebElement 对象，代表当前这一部电影的 DOM 节点（即 <div class="item"> 这个元素）
for movie in movies_item:

    # 从当前 movie 元素中，通过 XPath ".//span[@class='title']" 找到电影标题元素
    # ".//" 表示从当前节点（即 movie）开始，在它的所有子节点（包括嵌套）中查找
    # 这里找到的是第一部中文片名（因为 Top250 里通常第一个 title 是中文名）
    # .text 属性用于获取该元素中的纯文本内容
    movie_name = movie.find_element(By.XPATH, ".//span[@class='title']").text

    # 从当前 movie 元素中，通过 XPath ".//span[@class='rating_num']" 找到评分元素
    # 它的 text 就是评分数字（例如 9.7）
    rating = movie.find_element(By.XPATH, ".//span[@class='rating_num']").text

    # 从当前 movie 元素中，先找到包含链接的 <a> 标签，再提取它的 href 属性
    # 1. movie.find_element(...) 定位到 <a> 元素
    # 2. .get_attribute("href") 获取该元素的 href 属性值，即详情页的完整 URL
    movie_url = movie.find_element(By.XPATH, ".//div[@class='pic']/a").get_attribute("href")

    # 打印当前提取到的三部信息，便于在控制台观察进度和数据
    print(f"电影：{movie_name}")
    print(f"评分：{rating}")
    print(f"链接：{movie_url}")
    print("-" * 40)

    # 将当前电影的数据以字典形式添加到 all_movies 列表中
    # 字典的键是中文，方便后续理解，也便于直接写入 CSV 或 JSON
    all_movies.append({
        "标题": movie_name,
        "评分": rating,
        "链接": movie_url
    })


# ============================================================
# 第七步：输出汇总信息
# ============================================================

# 循环结束后，打印总共爬取了多少部电影
print(f"\n✅ 共爬取 {len(all_movies)} 部电影")


# ============================================================
# 第八步：等待并关闭浏览器
# ============================================================

# 让程序暂停 10 秒钟，目的是让你可以观察浏览器中的页面状态，确认数据是否正确
# 如果没有这一步，浏览器可能会在 driver.quit() 执行后立即关闭
time.sleep(10)

# 调用 driver.quit() 方法，关闭浏览器进程，释放系统资源
# 这是良好的编程习惯，避免后台残留多个浏览器进程
driver.quit()