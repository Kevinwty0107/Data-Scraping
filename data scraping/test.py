# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib
import csv
from urllib import request
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# !/usr/bin/python
# -*- coding: utf-8 -*-
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
divs = soup.find_all('tr', attrs={'class': 'with_building'})
print(divs)
tds = divs[0].findChildren('td')
print(tds[1].text)


#print(divs[0].text)

#driver.quit()
#a = driver.find_elements_by_class_name('Text')
#print(a)
#driver.find_elements_by_class_name("tabset-tab").click()

print("succeed")