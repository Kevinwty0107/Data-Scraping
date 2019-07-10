from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests


csvPath = "/Users/wangtaiyi/PycharmProjects/data/companydata.csv"
csvFile = open(csvPath, 'w')

writer = csv.writer(csvFile, dialect='excel')  # 写入对象

writer.writerow(["name", "description", "field", "Inv" , "value"])





def login(i):
    driver.get('https://www.itjuzi.com/login?url=%2F')
    time.sleep(3)
    driver.find_element_by_name('account').clear()
    driver.find_element_by_name('account').send_keys('15708947842')  # 这里填写你的用户名
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('947842')  # 这里填写你的密码
    time.sleep(2)
    driver.find_element_by_class_name('btn-primary').click()
    time.sleep(2)
    more = driver.find_elements_by_class_name('more')
    more[1].find_element_by_link_text('更多').click() # 这里填写你的密码
    windows = driver.window_handles
    driver.switch_to_window(windows[-1])
    time.sleep(3)
    #page = driver.find_elements_by_class_name('page-link')
    strs = []
    for k in range(i, 1000):
        strs.append(str(k))

    driver.find_element_by_link_text(strs[0]).click()
    time.sleep(3)
    print(driver.current_url)
    return driver.page_source




def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False



def scrap(soup):
    tbs = soup.find_all('tbody')
    trs = tbs[0].findChildren('tr')  # tr就是table中的每一行
    for tr in trs:
        tds = tr.findChildren('td')  # td是表格中的內容
        content = list()
        string = ""
        for td in tds:
            result = "," in td.text
            #print(result)
            if result == True:
                newtdtext = td.text.replace(",", "")
                #print(newtdtext)
                string = string + newtdtext
            else:
                temp = td.text
                #print(temp)
                string = string + temp

            string = string + ","

        csvFile.write(string)
        csvFile.write('\n')
        #print(string)




if __name__ == '__main__':
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.itjuzi.com/login?url=%2F')
    time.sleep(3)
    driver.find_element_by_name('account').clear()
    driver.find_element_by_name('account').send_keys('15708947842')  # 这里填写你的用户名
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('947842')  # 这里填写你的密码
    time.sleep(2)
    driver.find_element_by_class_name('btn-primary').click()
    time.sleep(2)
    more = driver.find_elements_by_class_name('more')
    more[1].find_element_by_link_text('更多').click()
    windows = driver.window_handles
    driver.switch_to_window(windows[-1])
    time.sleep(3)
    for i in range(1,1000):
        strs = []
        for k in range(i, 1000):
            strs.append(str(k))
        driver.find_element_by_link_text(strs[0]).click()
        print(driver.current_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        time.sleep(2)
        scrap(soup)
        time.sleep(2)
    driver.quit()
    csvFile.close()

