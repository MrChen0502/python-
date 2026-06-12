from lxml import html

# 读取html文件
with open("resources/tiobe页面代码.html", "r", encoding="utf-8") as f:
    html_text = f.read()
    # print(html_text)

    # 解析html的文本 将其转换为一个文本对象
    document =  html.fromstring(html_text)

    # 解析表头 - xpath语法
    # /table/thead/tr/th/text() ：表示从根节点开始匹配
    # //table/thead/tr/th/text() : 从任意位置开始匹配
    # th_list =  document.xpath("//table/thead/tr/th/text()")
    # th_list =  document.xpath("//table/thead/tr/th/text()")
    # print(th_list)

    # # tr[1] : 表示匹配第二个tr标签
    # td_list =  document.xpath("//tboy/tr[1]/td/text()")
    # print(td_list)


    # last() : 表示匹配最后一个
    td_list =  document.xpath("//tbody/tr[last()]/td/text()")
    print(td_list)

    # p[@arr] : 表示匹配p标签内的属性名 ==> p[@属性名]
    p_list =  document.xpath("//p[@class='']/text()")
    print(p_list)

    # * : 表示匹配任意标签
    th_list =  document.xpath("//thead/tr/*/text()")
    print(th_list)

    # @* : 表示匹配属性  * ==> 属性
    a_list =  document.xpath("//img/@src")
    print(a_list)