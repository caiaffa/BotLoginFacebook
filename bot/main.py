# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("YOUR DIRECTORY CHROME DRIVE")
browser.get("https://facebook.com") 
time.sleep(2)

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
 
username.send_keys("YOUR USERNAME")
password.send_keys("YOUR PASSWORD")
 
login_submit = browser.find_element_by_xpath("//*[@type='submit']")
login_submit.submit()