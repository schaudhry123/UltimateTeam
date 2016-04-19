from bs4 import BeautifulSoup
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json
import time
import signal

options = webdriver.ChromeOptions() 
options.add_extension('AdBlock_v2.44.crx')
browser = webdriver.Chrome('/Applications/chromedriver', chrome_options = options)

home_page = 'http://www.whoscored.com'
browser.get(home_page)
#browser.implicitly_wait(10)
#WebDriverWait(browser, 10).until(EC.presence_of_element_located(browser.find_element_by_id('popular-tournaments_list')))
elem = browser.find_element_by_id('popular-tournaments-list')
bullets = elem.get_attribute('href')
print(bullets.text)
print(elem.text)