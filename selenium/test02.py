#一组元素的定位
#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
file_path = 'file:///F:/TOOLS/%E6%B5%8B%E8%AF%95/TESThtml/checkbox.html'
browser.get(file_path)
inputs = browser.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(10)
browser.quit()

