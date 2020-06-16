#TestLoader

import testcase01
import testcase02
import unittest

def createsuite():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testcase01.test1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testcase02.test2)
    suite = unittest.TestSuite([suite1,suite2])
    return suite

if __name__ == '__main__':
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
