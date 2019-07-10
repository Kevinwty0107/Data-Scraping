# -*- coding: utf-8 -*-


import urllib
from bs4 import BeautifulSoup
import csv
import codecs
from urllib import request


with open("/Users/wangtaiyi/PycharmProjects/test.csv", "w", newline='') as c:
    #c.write(codecs.BOM_UTF8)
    #c.write(u'中文')
    #s='中文'
    writer = csv.writer(c, dialect='excel')  # 写入对象
    #writer.writerow([str.encode("goods"),str.encode("price"),str.encode("unit"), str.encode("location"),str.encode("time")])
    writer.writerow(['中文',"price","unit","location","time"])

    i = 1
    while i <= 4:
        print ("爬取第" + str(i) + "页")
        url = "http://www.gznw.gov.cn/priceInfo/getPriceInfoByAreaId.jx?areaid=22572&page=" + str(i)
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")
        print (soup.title.get_text())
        tt = soup.find_all("tr", class_="odd gradeX")
        for t in tt:
            content = t.get_text()
            num = content.splitlines()
            print (num[0], num[1], num[2], num[3], num[4], num[5])
            templist = []
            templist.append(num[1])
            templist.append(num[2])
            templist.append(num[3])
            templist.append(num[4])
            templist.append(num[5])
        # print templist
            writer.writerow(templist)
        i = i + 1

