from bs4 import BeautifulSoup
from urllib import request
import urllib

# 首先爬取跳蚤市场各个分类的入口链接

url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'

wb_data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(wb_data, 'html.parser')
mainUrlStrs = soup.select('.sider > .fenlei > dt > a')
for mainUrlStr in mainUrlStrs:
        if mainUrlStr.get('href') == "/shouji/" \
                or mainUrlStr.get('href') == "/diannao/" \
                or mainUrlStr.get('href') == "/jiaju/" \
                or mainUrlStr.get('href') == "/xianzhilipin/" \
                or mainUrlStr.get('href') == "/xuniwupin/":
            mainUrlStrs.remove(mainUrlStr)
        else:
            print(url_host + mainUrlStr.get('href'))

    # 根据入口链接爬取商品信息，同时写入

from bs4 import BeautifulSoup
import request
import random
import csv
# from pageList import get_list_info
#  from mainUrl import urlStr

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Connection': 'keep-alive'
    }
# 随机IP，因为同一个IP频繁请求，服务器将会视其为黑客攻击，所有我们会随机分配IP来请求
proxy_list = [
        'http://125.88.74.122:85',
        'http://125.88.74.122:83',
        'http://171.8.79.143:8080',
        'http://14.152.93.79:8080',
    ]
proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
proxies = {'http': proxy_ip}
with open("/Users/wangtaiyi/PycharmProjects/data/test1.csv", "w", newline='') as c:
    writer = csv.writer(c, dialect='excel')  # 写入对象
    writer.writerow(["title", "price", "location"])
    for p in range(1 ,100):
        print("爬取第" + str(p) + "页")
        url = 'http://bj.ganji.com/bangong/'+'o' + str(p)
        if soup.find('div', 'no-search') or soup.find('div', 'noinfo'):
            print('已经到最后一页')
            pass
        wb_data2 = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(wb_data2, 'html.parser')
        # 二手设备
        print('二手设备')
        titles = soup.select('.js-item > a')
        prices = soup.select('.pt-price > span')
        locations = soup.select('.feature > span')
        for title, price, location in zip(titles, prices, locations):
            print(title.text) if len(title.text) != 0 else print('None')
            print(price.text) if len(price.text) != 0 else print('None')
            print(location.text) if len(location.text) != 0 else print('None')
            infoTitle = title.text if len(title.text) != 0 else print('None')
            infoPrice = price.text if len(price.text) != 0 else print('None')
            infoLocation = location.text if len(location.text) != 0 else 'None'
            templist = []
            templist.append(infoTitle)
            templist.append(infoPrice)
            templist.append(infoLocation)
            # print templist
            writer.writerow(templist)





