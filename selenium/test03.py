#多层框架定位
from selenium import webdriver
import time

browser = webdriver.Firefox()
file_path = 'file:///F:/TOOLS/%E6%B5%8B%E8%AF%95/TESThtml/frame.html'
browser.get(file_path)
browser.implicitly_wait(20)
browser.switch_to.frame("f1")
browser.switch_to.frame("f2")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").submit()
time.sleep(6)
browser.switch_to.default_content()
browser.switch_to.frame("f1")
time.sleep(6)
browser.find_element_by_xpath("/html/body/div/div/a")
time.sleep(5)
browser.quit()
