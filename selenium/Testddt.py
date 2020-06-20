# 测试数据驱动ddt

from ddt import ddt, data, unpack,file_data
from selenium import webdriver
import unittest
import time


@ddt
class ddtTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://www.baidu.com/"


# 清除环境
def tearDown(self):
    self.driver.quit()


# @unittest.skip("skipping")
# @data('selenium', u'蔡徐坤', u'乐山大佛')
def test_testddt(self, value):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.find_element_by_id("kw").click()
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(value)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    print(value)


# @unpack
@data(['selenium', u'selenium_百度搜索'], [u'蔡徐坤', u'蔡徐坤_百度搜索'], [u'乐山大佛', u'乐山大佛_百度搜索'])
def test_hao(self, value, expected_value):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.find_element_by_id("kw").click()
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(value)
    driver.find_element_by_id("su").click()
    time.sleep(2)
    self.assertEqual(expected_value, driver.title)
    print(expected_value, driver.title)


if __name__ == "__main__":
    unittest.main()
