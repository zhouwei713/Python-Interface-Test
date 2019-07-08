# coding = utf-8
"""
@author: zhou
@time:2019/7/3 14:48
"""

from base.basetest import BaseTest, CaseData
import pytest


class Test_example(BaseTest):
    testcase = CaseData('test.xlsx', 1)
    testdata, ids = testcase.get_testcase_data()

    @pytest.mark.parametrize('autotest', testdata['parameterize'], ids=ids)
    def test_case(self, autotest, casefile):
        res_json = self.runmethod.run_main(autotest['request-data']['method'], autotest['request-data']['url'],
                                           data=autotest['request-data']['data'],
                                           header=autotest['request-data']['header'])
        print(res_json)
        print("casefile", casefile)
        assert self.validate.is_equal_dict(res_json, autotest['response-data']['checkpoint']) is True


