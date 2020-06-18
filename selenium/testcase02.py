#unitest
from selenium import webdriver
import unittest


class test2(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://www.baidu.com/"

    # 清除环境
    def tearDown(self):
        self.driver.quit()

    @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"测试")
        driver.find_element_by_id("su").click()

    if __name__ == "__main__":
        #执行测试用例
        unittest.main()