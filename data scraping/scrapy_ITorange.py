import os
from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests


os.chdir(u'/Users/zhoutong/Desktop/sohu/08_ADP/15_分析/03_2019品牌重点行业分析/')
writeobj = open("data.csv",'w+')


def scrap(soup):
    tbs = soup.find_all('tbody')
    trs = tbs[0].findChildren('tr')  # tr就是table中的每一行
    for tr in trs:
        tds = tr.findChildren('td')  # td是表格中的內容
        # print tds
        name = tds[1].find_all('a')[1].text
        detail = tds[1].find('div').text.strip().replace('\n', '.')
        industry = tds[2].text
        invest = tds[3].text
        income = tds[4].text
        return_str = '|'.join([name, detail, industry, invest, income])
        
        print (return_str)

        writeobj.write(return_str.encode('utf8')+'\n')


if __name__ == '__main__':
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # 登录
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.itjuzi.com/login?url=%2F')
    driver.find_element_by_name('account').clear()
    driver.find_element_by_name('account').send_keys('15708947842')  # 这里填写你的用户名
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('947842')  # 这里填写你的密码
    ## 点击
    driver.find_element_by_class_name('btn-primary').click()
    time.sleep(1)
    ## 模拟点击公司更多
    more = driver.find_elements_by_class_name('more')
    more[1].find_element_by_link_text('更多').click()
    windows = driver.window_handles
    driver.switch_to_window(windows[-1])
    time.sleep(1)
    # scrape
    for i in range(1,6092):
        print(driver.current_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        time.sleep(1)
        scrap(soup)
        time.sleep(1)
        # 判断是否成功
        success = False
        while not success:
            try:
                # 滑到页面底端 保证获取到页码
                js="var q=document.documentElement.scrollTop=100000" 
                driver.execute_script(js)
                # 模拟点击下一页
                driver.find_elements_by_class_name('page-item')[-2].click()
                success = True
                print ('\n'+ '=='*5 + u'已爬取完成第%s页' %str(i) + '=='*5  + '\n')
            except Exception as e:
                # 打印错误信息
                print ('exception:' + str(Exception))
                print ('\n'+ '==' *5 + '重试中' + '==' *5 + '\n')
                time.sleep(5)

    writeobj.close()
    driver.quit()


