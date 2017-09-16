# coding=utf-8
import re  # 正则
import requests  #获取网页
import pymysql   #数据库

# 首先获取首页上所有分类频道链接
def main_url(url):
    # 创建一个列表存放链接
    CategoryLink = list()
    mainurl = requests.get(url)
    url = mainurl.content
    #print url
    Regular = 'a data-key="\d{1,5}" href="(/s.*?g{1}\d{1,5})"'
    pic_url = re.findall(Regular, url, re.S)
    print pic_url
    for link in pic_url:
        urll = 'http://www.dianping.com' + link
        print urll
        CategoryLink.append(urll)

    return CategoryLink

# 获取每个分类 第一页所有店铺的名字和三项评分以及地址

# 将信息放进数据库





#主控
def main():
    mainurl = main_url('http://www.dianping.com/shanghai')

if __name__ == '__main__':
    main()
