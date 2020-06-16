#makesuite

import testcase01
import testcase02
import unittest

def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testcase01.test1))
    suite.addTest(unittest.makeSuite(testcase02.test2))
    return suite
if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)