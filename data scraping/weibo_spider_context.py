#!/usr/bin/env python
#coding=utf-8
#python version：3.6
#author:taiyiwang

import time
import os
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS
from lxml import etree
import xlwt
import xlrd
from xlutils.copy import copy
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#os.chdir("C:/Users/xulingzhang/Desktop")
os.chdir("/Users/zhoutong/Desktop/sohu/jd_11")


def login_weibo(username, password):
    try:
        #输入用户名/密码登录
        print (u'准备登陆Weibo.cn网站...')
        driver.get("https://passport.weibo.cn/signin/login?entry=mweibo") 
        #elem_user = driver.find_element_by_id("loginName")  # 定位用户名输入框，方法1
        elem_user = driver.find_element_by_xpath("/html/body/div/form/section/div/p/input")  # 定位用户名输入框，方法2
        time.sleep(2)
        elem_user.clear()
        elem_user.send_keys(username) #用户名
        elem_pwd = driver.find_element_by_id("loginPassword")
        elem_pwd.send_keys(password)  #密码
        #elem_rem = driver.find_element_by_name("remember")
        #elem_rem.click()             #记住登录状态

        #重点: 暂停时间输入验证码
        #pause(millisenconds)
        time.sleep(2)

        elem_sub = driver.find_element_by_id("loginAction")
        elem_sub.click()              #点击登陆
        time.sleep(5)
        
        #print driver.current_url
        #print driver.get_cookies()  #获得cookie信息 dict存储
        #print u'输出Cookie键值对信息:'
        #for cookie in driver.get_cookies(): 
        #    for key in cookie:
        #        print key, cookie[key]         
        #driver.get_cookies()类型list 仅包含一个元素cookie类型dict
        
        print (u'登陆成功...')
              
    except Exception as e:
        print ("Error: ",e)
    finally:    
        print (u'End LoginWeibo!\n\n')


def get_word_list():
    word_list = []
    for line in open("baoma_wd_pkg.txt"):
        fields = line.strip().split('\t')
        if len(fields) != 1:
            continue
        query_wd, = [f.strip() for f in fields]
        word_list.append(query_wd)
    return word_list

def init_weibo_context_dict():
    return {'nick_name':'',
             'domain_url':'',
             'weibo_context':''}


def spider_weibo_context(wd,max_page,writeobj):
    
    #url = "https://m.weibo.cn/p/100103type%3D1%26q%3D" + wd
    #url = "http://s.weibo.com/weibo/" + wd+'&page='

    filter_set = set([])
    url = "http://weibo.cn/search/"
    driver.get(url)
    
    input_form = driver.find_element_by_name("keyword")
    input_form.send_keys(wd)
    time.sleep(2)   
    input_buttern = driver.find_element_by_name("smblog")
    input_buttern.click()             
    time.sleep(2)

    page = 1
    while True:
        user_list = driver.find_elements_by_class_name("nk")   # driver.find_elements_by_xpath("/html/body/div/div/a")
        weibo_list = driver.find_elements_by_class_name("ctt")  # driver.find_elements_by_xpath("/html/body/div/div/span")

        for i in range(len(user_list)):
            nick_name = user_list[i].text
            domain_url =  user_list[i].get_attribute('href')
            weibo_context = weibo_list[i].text
            weibo_context = weibo_context.replace('\n',' ')
            
            if nick_name not in filter_set: # wd in weibo_context and 
                spider_output_str = '\t'.join([nick_name,domain_url,weibo_context])
                writeobj.write(wd.encode('utf8') + '\t' + spider_output_str.encode('utf8') + '\n')
                print (domain_url)

            filter_set.add(nick_name)

           
        if page == max_page:
            break
        try:
            next_buttern = driver.find_element_by_link_text("下页")
            next_buttern.click()
            page += 1  
        except:
            break
        '''
        
        if page == max_page:
            break
        page += 1
        url = "https://weibo.cn/search/mblog?hideSearchFrame=&keyword="
        url += quote(wd.encode('utf8'))+"&page="+str(page)
        driver.get(url)
        '''

        time.sleep(3)



if __name__ == '__main__':
    
    driver = webdriver.Firefox()
    wait = ui.WebDriverWait(driver,10)

    login_weibo("djh_53202@126.com", "cherry24680")

    #word_list = get_word_list()
    #word_list = [ u"5系",u"bmw新5系",u"bmw5系",u"宝马5系",u"宝马新5系",u"宝马5",u"宝马gt",u"五系gt",u"宝马m5",u"宝马suv5系",u"宝马进口5系",u"宝马五系",u"宝马新款五系",
    #             u"华晨宝马5",u"新bmw",u"新宝马5",u"新宝马5系",u"宝马x5"]   #
    word_list = [u"京东618"]

    writeobj = open("weibo_context_all.res",'w+')
    
    for wd in word_list:
        spider_weibo_context(wd,50,writeobj)
        time.sleep(10)

    writeobj.close()
    driver.quit()

    

