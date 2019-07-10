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


baseUrl = "https://streeteasy.com/search?utf8=%E2%9C%93&search=1+BOGARDUS+PLACE"
url_host= "https://streeteasy.com"
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
    divs = soup.find_all('div',attrs={'class': 'tabset-content'})
    #if len(divs) < 0 or len(divs) == 0:
     #   print ("No div class named " + str('full u-positionStatic'))
     #   return
    divs2 = divs[0].find_all('div',attrs={'class':'tabset-content selected'})
    print(divs2[0])
    tbs = divs2[0].findChildren('tbody')
    print (tbs[0])
    trs = tbs[0].findChildren('tr') # tr就是table中的每一行
    for tr in trs:
        tds = tr.findChildren('td')  # td是表格中的內容
        content = list()
        string = ""
        print(tr)

        index = 0  # 判斷漢字出現的位置
        for td in tds:
            temp = td.text
            print(temp)
            if index == 7 or index == 0:
                temp2 = ""
                for d in temp:
                    if not is_chinese(d):  # 去除漢字
                        temp2 += d
                temp = temp2

            string = string + temp
            string = string + ","
            index += 1

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
        #content = list()
        #string = ""
        #print (tr)

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


#.Container >.search-results >.line-result >
#divs = soup.find_all('div', attrs={'class': 'description'})
#b = divs[0].findChildren('b')
#a = b[0].findChildren('a')
#mainUrlStrs = a[0].get('href')
#print (mainUrlStrs)
#for mainUrlStr in mainUrlStrs:
    #拼接
#    print(url_host + mainUrlStr.get('href'))

#print(mainUrlStrs[0])

#url = url_host + mainUrlStrs[0].get('href')



from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)

driver = webdriver.PhantomJS(executable_path="/Applications/phantomjs/bin/phantomjs",desired_capabilities=dcap)
#driver = webdriver.ChromeOptions()
driver.get("https://streeteasy.com/building/1-bogardus-place-new_york#tab_building_detail=3")
print("succeed")
time.sleep(3)
driver.maximize_window()
#driver.switch_to.frame("building-tabs")
driver.find_elements_by_class_name("tabset-tab").click()#这一步骤不知道能不能成功
time.sleep(10)
response = driver.page_source
driver.quit()

wb_data = requests.get("https://streeteasy.com/building/1-bogardus-place-new_york#tab_building_detail=3",headers=headers)
#soup = BeautifulSoup(wb_data.text, 'html.parser')
#wb_data = urllib.request.urlopen("https://streeteasy.com/building/1-bogardus-place-new_york#tab_building_detail=3").read()
soup2 = BeautifulSoup(wb_data.text,"html.parser")
print(soup2)
getprice(soup2)
print ("Finished!")
csvFile.close()
