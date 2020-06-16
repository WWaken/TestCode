#Html报告的生成

import sys
import time
import unittest
import HTMLTestRunner

def createsuite():
    discover = unittest.defaultTestLoader.discover("../selenium",pattern='testcase*.py',top_level_dir=None)
    return discover

if __name__ == '__main__':
    curpath = sys.path[0]
    print(sys.path)
    print(curpath)
    now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))

    filename = curpath + '/resultreport'+now+'resultreport.html'
    with open(filename,"wb") as fp:
        runner =HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='测试报告',description='执行用例测试情况')
        suite = createsuite()
        runner.run(suite)

