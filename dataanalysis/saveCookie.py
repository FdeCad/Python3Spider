import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)

url = "http://hotel.qunar.com/"
brower.get(url)
bcookies  = brower.get_cookies()

cookies_nologin = {}
for item in bcookies:
    cookies_nologin[item['name']] = item['value']
print(cookies_nologin)
print("\n\n")


time.sleep(30)#页面做登录操作
bcookies  = brower.get_cookies()

cookies = {}
for item in bcookies:
    cookies[item['name']] = item['value']
    outputPath = open('cookie.pickle','wb')
    pickle.dump(cookies,outputPath)
#print(browser.get_cookies())
print(cookies)
print("\n\n")