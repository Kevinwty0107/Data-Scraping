# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib
import csv
from urllib import request
import time


#baseUrl = "https://streeteasy.com/search?utf8=%E2%9C%93&search=1+BOGARDUS+PLACE"
#url_host= "https://streeteasy.com"
#这里还要加入如何搜索baseUrl，如果搜索不到怎么办

csvPath = "/Users/wangtaiyi/PycharmProjects/data/PriceData.csv"
csvFile = open(csvPath, 'w')
#writer = csv.writer(csvFile, dialect='excel')  # 写入对象

#writer.writerow(["data", "unit", "rent", "beds", "Baths","ft","floorplan"])
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def getprice(soup):
    tbs = soup.find_all('tbody', attrs={'class': 'building_availabilities'})
    #print (tbs[0])
    trs = tbs[0].findChildren('tr') # tr就是table中的每一行
    for tr in trs:
        tds = tr.findChildren('td')  # td是表格中的內容
        content = list()
        string = ""
        print(tr)
        for td in tds:
            result = "," in td.text
            print (result)
            if result == True:
                newtdtext = td.text.replace(",","")
                print(newtdtext)
                string = string + newtdtext
            else:
                temp = td.text
                print(temp)
                string = string + temp

            string = string + ","

            # content.append(td.text)
        # print content
        # string = string[:-1]
        print(string)
        csvFile.write(string)
        csvFile.write('\n')
        #content = tds.get_text()
        #num = content.splitlines()
        #print(num[0], num[1], num[2], num[3], num[4], num[5])
        #templist = list()
        #templist.append(num[1])
        #templist.append(num[2])
        #templist.append(num[3])
        #templist.append(num[4])
        #templist.append(num[5])
        # print templist
        #writer.writerow(templist)

import requests
import random

#headers信息
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



from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

driver = webdriver.Chrome(executable_path="/Applications/Chrome/chromedriver",chrome_options=options)
#driver = webdriver.ChromeOptions()
driver.get("https://rentlogic.com/")
#driver.find_element_by_class_name("header-search-input rentlogic_search mobile-hide").clear()
driver.find_elements_by_class_name("header-search-input")[1].send_keys('1 BOGARDUS PLACE')
time.sleep(3)
driver.find_elements_by_class_name("header-search-input")[1].send_keys(Keys.ENTER)
#driver.find_elements_by_class_name("lens")[0].click()
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response,"html.parser")
getprice(soup)
print ("Finished!")
csvFile.close()
