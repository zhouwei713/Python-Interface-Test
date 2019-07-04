# coding = utf-8
"""
created on 20181009

@author: zhou
"""

from case.testcase import testinterface
from interface.get_excel import data
import os
import datetime
import time
from tools.get_data import GetExcelData


def start_test():
    starttime = datetime.datetime.now()
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir = os.path.abspath(os.path.dirname(__file__))
    file = os.getcwd() + '/data/case.xlsx'
    testid, testname, testkey, testparam, testurl, testmode, testexcept = data(file)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi = testinterface()
    filepath = os.path.join(basdir+'/report/%s-result.html' % day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime = datetime.datetime.now()
    print(basdir, filepath)


if __name__ == '__main__':
    import pytest
    pytest.main(['-s', '-q', '-vv', '--html=./report/report.html', '--self-contained-html'])
    # pytest --html=report.html --self-contained-html  生成独立的测试报告
    # data = GetExcelData(filename='case1.xlsx')
    # print(data.get_case_lines())
    # start_test()
    # testinterface()


