from selenium import webdriver  # 导入webdriver包
from selenium.webdriver import ActionChains  # 模拟鼠标操作
from selenium.webdriver.common.by import By  # 按照什么方式去查找
from selenium.webdriver.common.keys import Keys  # 模拟键盘操作


# 1 模拟浏览器访问京东页面，解决翻爬虫
def spider(url, keyword):
    driver = webdriver.Safari()  # 打开safari浏览器
    print(keyword)


# 2 定位商品抓取数据
# 3 大量的数据

if __name__ == '__main__':
    spider('www.jd.com', '口罩')
