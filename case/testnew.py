# coding = utf-8
"""
@author: zhou
@time:2019/7/3 14:48
"""

import unittest
from base import HTMLTestRunner


class MyTest(unittest.TestCase):
    def test_run1(self):
        self.assertIs(1, 1)

    def test_run2(self):
        self.assertIs(1, 2)


if __name__ == '__main__':
    # unittest.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest(MyTest('test_run1'))
    fp = open('res.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test测试报告', description='测试情况')
    runner.run(test_suite)
    fp.close()
