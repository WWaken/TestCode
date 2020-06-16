#addTest构建测试套件

import testcase01
import testcase02
import unittest

def createsuite():
    suite = unittest.TestSuite()
    #将测试用例加入到测试容器（套件）中
    suite.addTest(testcase01.test1("test_baidusearch"))
    suite.addTest(testcase02.test2("test_baidusearch"))
    suite.addTest(testcase01.test1("test_hao"))
    return suite
if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)