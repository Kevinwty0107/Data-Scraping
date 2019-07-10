from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(executable_path="/Applications/Chrome/chromedriver",chrome_options=options)

driver.get('https://qzone.qq.com/')
#driver.switch_to.frame('login_frame')
#driver.find_element_by_id('switcher_plogin')

driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('819048329')  #这里填写你的QQ号
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('qwertyuiop')  #这里填写你的QQ密码
driver.find_element_by_id('login_button').click()
response = driver.page_source
abtract_pattern = re.compile('<a target="_blank" href="http://user.qzone.qq.com/(.\d*)" data-clicklog="nick" class="f-name q_namecard " link="nameCard_(.\d*)">(.*?)</a>',re.S)
abtract = re.findall(abtract_pattern, str(response))
elements = driver.find_elements_by_class_name('f-info')
i = 0
for a in abtract:
    print(a[2] + "  :  " + elements[i].text)
    i = i + 1