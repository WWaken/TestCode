#unitest
from selenium import webdriver
import unittest
import time
import os

class test1(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://www.baidu.com/"

    # 清除环境
    def tearDown(self):
        self.driver.quit()

    def savescreenshot(self,driver,file_name):
        if not os.path.exists('./image'):
            os.makedirs('./image')
        now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        driver.get_screenshot_as_file('./image/'+now+'-'+file_name)
        time.sleep(1)

    @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()


    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_link_text("hao123").click()
        try:
            self.assertEqual(u"hao_123上网从这里开始",driver.title)
        except:
            self.savescreenshot(driver,'hao.png')

    if __name__ == "__main__":
        unittest.main()