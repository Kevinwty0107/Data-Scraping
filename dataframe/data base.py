from bs4 import BeautifulSoup
import requests

url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'html.parser')
mainUrlStrs = soup.select('.fenlei > dt > a')

for mainUrlStr in mainUrlStrs:
    #拼接
    print(url_host + mainUrlStr.get('href'))

from bs4 import BeautifulSoup
import requests
import random
import pymongo

#连接mongoDB数据库
#参数localhost:表示在本地数据库
#参数27017：端口，表示指向哪
client = pymongo.MongoClient('localhost',27017)
#创建数据库名称
ganjiwang = client['ganjiwang']
#创建数据表
list_info = ganjiwang['list_info']

#赶集网headers信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Connection':'keep-alive'
}

#随机IP，因为同一个IP频繁请求，服务器将会视其为黑客攻击，所有我们会随机分配IP来请求
proxy_list = [
    'http://125.88.74.122:85',
    'http://125.88.74.122:83',
    'http://171.8.79.143:8080',
    'http://14.152.93.79:8080',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}

#爬取网页信息的核心代码，该函数可以写的有点笨，可再次做优化，这里只为实现需求，不再优化
def get_list_info(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    # print(soup)
    #当是该类商品最后一页是，即没有更多商品时，我们pass掉
    if soup.find('div','no-search') or soup.find('div','noinfo'):
        print('已经到最后一页')
        pass
    elif url.find('http://bj.ganji.com/bangong/') == 0:
        #二手设备
        print('二手设备')
        titles = soup.select('.js-item > a')
        imgs = soup.select('.list-bigpic > dt > a > img')
        prices = soup.select('.pt-price > span')
        locations = soup.select('.feature > span')
        for title,img,price,location in zip(titles,imgs,prices,locations):
            print(title.text)
            print(title.get('href'))
            print(img.get('data-original')) if img.get('data-original') else print(img.get('src'))
            print(price.text)
            print(location.text) if len(location.text) != 0 else print('无')
            infoTitle = title.text
            infoDetailUrl = title.get('href')
            infoImgUrl = img.get('data-original') if img.get('data-original') else img.get('src')
            infoPrice = price.text
            infoDetailText = '无'
            infoLocation = location.text if len(location.text) != 0 else '无'
            #写入数据库
            list_info.insert_one({'title':infoTitle,
                                  'detailUrl':infoDetailUrl,
                                  'img':infoImgUrl,
                                  'price':infoPrice,
                                  'detailText':infoDetailText,
                                  'location':infoLocation})

    elif url.find('http://bj.ganji.com/nongyongpin/') == 0:
        #二手农用品
        # print('二手农用品')
        titles = soup.select('.js-item > a')
        imgs = soup.select('.list-bigpic > dt > a > img')
        prices = soup.select('.pt-price > span')
        locations = soup.select('.list-word > a')
        for title,img,price,location in zip(titles,imgs,prices,locations):
            print(title.text)
            print(title.get('href'))
            print(img.get('data-original')) if img.get('data-original') else print(img.get('src'))
            print(price.text)
            print(location.text) if len(location.text) != 0 else print('无')
            infoTitle = title.text
            infoDetailUrl = title.get('href')
            infoImgUrl = img.get('data-original') if img.get('data-original') else img.get('src')
            infoPrice = price.text
            infoDetailText = '无'
            infoLocation = location.text if len(location.text) != 0 else '无'
            list_info.insert_one({'title':infoTitle,
                                  'detailUrl':infoDetailUrl,
                                  'img':infoImgUrl,
                                  'price':infoPrice,
                                  'detailText':infoDetailText,
                                  'location':infoLocation})

    elif url.find('http://bj.ganji.com/xianzhilipin/') == 0:
        #二手闲置礼品
        print('二手闲置礼品')
        titles = soup.select('.js-item > a')
        imgs = soup.select('.list-bigpic > dt > a > img')
        prices = soup.select('.pt-price > span')
        details = soup.select('.feature > p')
        locations = soup.select('.list-word > a')
        for title,img,price,detail,location in zip(titles,imgs,prices,details,locations):
            print(title.text)
            print(title.get('href'))
            print(img.get('data-original')) if img.get('data-original') else print(img.get('src'))
            print(price.text)
            print(detail.text)
            print(location.text)
            infoTitle = title.text
            infoDetailUrl = title.get('href')
            infoImgUrl = img.get('data-original') if img.get('data-original') else img.get('src')
            infoPrice = price.text
            infoDetailText = detail.text
            infoLocation = location.text if len(location.text) != 0 else '无'
            list_info.insert_one({'title':infoTitle,
                                  'detailUrl':infoDetailUrl,
                                  'img':infoImgUrl,
                                  'price':infoPrice,
                                  'detailText':infoDetailText,
                                  'location':infoLocation})

    elif url.find('http://bj.ganji.com/xuniwupin/') == 0:
        #二手虚拟物品
        print('二手虚拟物品')
        titles = soup.select('.js-item > a')
        imgs = soup.select('.list-bigpic > dt > a > img')
        prices = soup.select('.pt-price > span')
        details = soup.select('.feature > p')
        locations = soup.select('.list-word > a')
        for title,img,price,detail,location in zip(titles,imgs,prices,details,locations):
            print(title.text)
            print(title.get('href'))
            print(img.get('data-original')) if img.get('data-original') else print(img.get('src'))
            print(price.text)
            print(detail.text)
            print(location.text)

            infoTitle = title.text
            infoDetailUrl = title.get('href')
            infoImgUrl = img.get('data-original') if img.get('data-original') else img.get('src')
            infoPrice = price.text
            infoDetailText = detail.text
            infoLocation = location.text if len(location.text) != 0 else '无'
            list_info.insert_one({'title':infoTitle,
                                  'detailUrl':infoDetailUrl,
                                  'img':infoImgUrl,
                                  'price':infoPrice,
                                  'detailText':infoDetailText,
                                  'location':infoLocation})
    else:
        #非二手设备、二手农用品
        titles = soup.select('.t > a')
        imgs = soup.select('.js-lazy-load')
        prices = soup.select('.pricebiao > span')
        details = soup.select('.desc')
        locations = soup.select('#infolist > div.infocon > table > tbody > tr > td.t > span.fl')
        for title,img,price,detail,location in zip(titles,imgs,prices,details,locations):
            print(title.text)
            print(title.get('href'))
            print(img.get('data-original')) if img.get('data-original') else print(img.get('src'))
            print(price.text)
            print(detail.text)
            print(location.text) if len(location.text) != 0 else print('无')
            infoTitle = title.text
            infoDetailUrl = title.get('href')
            infoImgUrl =  img.get('data-original') if img.get('data-original') else img.get('src')
            infoPrice = price.text
            infoDetailText = detail.text
            infoLocation = location.text if len(location.text) != 0 else '无'
            list_info.insert_one({'title':infoTitle,
                                  'detailUrl':infoDetailUrl,
                                  'img':infoImgUrl,
                                  'price':infoPrice,
                                  'detailText':infoDetailText,
                                  'location':infoLocation})


from multiprocessing import  Pool

#因为在观察赶集网的链接是我们发现o1..o2..是对应页面的页码，所有这里拼接每个页面的链接，这里以最多100页为测试
def get_all_list_info(url):
    for p in range(1,100):
        get_list_info(url + 'o' + str(p))


if __name__ == '__main__':#需加上这句代码，这时是一种固定的写法，作用是这句代码会把他上下分开两部分，避免我们改变地址时的名字混乱
    # 创建一个进程池，所有我们设计的爬虫，都会被放到进程池内，然后自动分配系统资源来执行
    # pool()有一个参数，processes，表示有多少个进程,比如processes=2
    pool = Pool()
    # 从所有频道列表中得到链接，
    # map()函数：会把后面的集合一个一个的放到第一个函数中执行
    # 参数1:一个函数
    # 参数2:一个集合
    for mainUrlStr in mainUrlStrs:
        # 拼接
        Urlstr = url_host + mainUrlStr.get('href')
        pool.map(get_all_list_info,Urlstr.split())
    pool.close()
    pool.join()



