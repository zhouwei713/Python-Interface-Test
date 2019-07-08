"""
created on 20181012
@author: zhou
"""

import xlrd


def data(filepath):
    try:
        file = xlrd.open_workbook(filepath)
        page = file.sheets()[0]
        nrows = page.nrows
        testid = []
        testname = []
        testkey = []
        testparam = []
        testurl = []
        testmode = []
        testexcept = []
        for i in range(1, nrows):
            testid.append(page.cell(i, 0).value)
            testname.append(page.cell(i, 1).value)
            testkey.append(page.cell(i, 2).value)
            testparam.append(page.cell(i, 3).value)
            testurl.append(page.cell(i, 4).value)
            testmode.append(page.cell(i, 5).value)
            testexcept.append(page.cell(i, 6).value)
        return testid, testname, testkey, testparam, testurl, testmode, testexcept
    except Exception as e:
        print('open case data error: %s' % e)
        return




