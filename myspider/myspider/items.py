# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scr
#


    # user_agent  设置ua
    # coucurrent requests  设置并发请求的
#     download-delay  i下载延迟，默认无延迟
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/clicks.htm')

click_btn = driver.find_element_by_xpath('//input[@value="click me"]')
doubleclick_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')
rightclick_btn = driver.find_element_by_xpath('//input[@value="right click me"]')

ActionChains(driver).click(click_btn).double_click(doubleclick_btn).context_click(rightclick_btn).perform()

print (driver.find_element_by_name('t2').get_attribute('value'))

sleep(2)
driver.quit()