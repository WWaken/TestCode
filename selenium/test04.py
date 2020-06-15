#层级定位
from selenium import webdriver
import time

browser = webdriver.Firefox()
file_path = 'file:///F:/TOOLS/%E6%B5%8B%E8%AF%95/TESThtml/level_locate.html'
browser.get(file_path)
browser.find_element_by_xpath('/html/body/div[1]/div/div/a').click()
browser.implicitly_wait(15)
# browser.find_elements_by_id('dropdown1').is_displayed()
br = browser.find_element_by_id('dropdown1').find_element_by_link_text('Action')
webdriver.ActionChains(browser).move_to_element(br).perform()
time.sleep(5)
browser.quit()



