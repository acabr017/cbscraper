from bs4 import BeautifulSoup
#import requests
#from urllib.request import urlopen
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



PATH = 'C:\Program Files (x86)\chromedriver.exe'
sign_in_url = 'https://account.collegeboard.org/login/login'
driver = webdriver.Chrome(PATH)
driver.get(sign_in_url)
time.sleep(1)
username = driver.find_element_by_id('username')
username.send_keys()
password = driver.find_element_by_id('password')
password.send_keys()
button = driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[1]/button')
button.click()

cb_url = 'https://apclassroom.collegeboard.org/92/assessments/results/44812277/questions'
driver.get(cb_url)

import pdb; pdb.set_trace()

cb_html = driver.find_element_by_xpath('//*').get_attribute("outerHTML")
cb_soup = BeautifulSoup(cb_html,'html.parser')

import pdb; pdb.set_trace()