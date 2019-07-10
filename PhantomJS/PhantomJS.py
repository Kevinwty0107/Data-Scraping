# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib
from urllib import request
import time

baseUrl = "http://stock.finance.sina.com.cn/option/quotes.html"
csvPath = "/Users/wangtaiyi/PycharmProjects/data/FinanceData.csv"
csvFile = open(csvPath, 'w')

def is_chinese(uchar):
        # 判断一个unicode是否是汉字
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

#def readPage(url):
    #webURL = urllib.request.urlopen(baseUrl)
    #content = webURL.read()
    #soup = BeautifulSoup(content)
    #return soup

def getFinance(soup, tableName):
    divs = soup.findAll('div', attrs={'class': tableName}) #看涨合约在这个div中
    if len(divs) < 0 or len(divs) == 0:
        print ("No div class named " + str(tableName))
        return
    tbs = divs[0].findChildren('tbody') # 獲取tbody內容，在這個標籤下只有一個tbody
    print (tbs[0])
    trs = tbs[0].findChildren('tr') # tr就是table中的每一行
    for tr in trs:
        tds = tr.findChildren('td') # td是表格中的內容
        content = list()
        string = ""
        print (tr)

        index = 0 # 判斷漢字出現的位置
        for td in tds:
            temp = td.text
            print (temp)
            if index == 7 or index == 0:
                temp2 = ""
                for d in temp:
                    if not is_chinese(d): # 去除漢字
                        temp2 += d
                temp = temp2

            string = string + temp
            string = string + ","
            index += 1

            #content.append(td.text)
        #print content
        #string = string[:-1]
        print (string)
        csvFile.write(string)
        csvFile.write('\n')

tableName = "table_down fr" # 表格名稱

driver = webdriver.PhantomJS(executable_path="/Applications/phantomjs/bin/phantomjs")
driver.get(baseUrl)

####################################################
# wait 10s until the specified table name presents
try:
# 看涨合约和看跌合约的表格是一个class，要用CLASS_NAME指定
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, tableName)))
except Exception as e:
    print (e)
finally:
    data = driver.page_source # 取到加載js後的頁面content
    driver.quit()
####################################################

#soup = readPage(loadUrl)
soup = BeautifulSoup(data,"html.parser")
getFinance(soup, tableName)
print ("Finished!")
csvFile.close()