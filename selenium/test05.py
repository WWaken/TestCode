#下拉框处理
from selenium import webdriver
import time

browser = webdriver.Firefox()
file_path = 'file:///F:/TOOLS/%E6%B5%8B%E8%AF%95/TESThtml/drop_down.html'
browser.get(file_path)
D = browser.find_element_by_id('ShippingMethod')
time.sleep(10)
D.find_element_by_xpath("//*[@id='ShippingMethod']/option[5]").click()
time.sleep(5)
# # options = browser.find_elements_by_tag_name('option')
# #options[5].click()
# for option in options:
#     if option.get_attribute('value') == "9.25":
#         option.click()
# time.sleep(10)
browser.quit()




