# coding = utf-8
"""
@author: zhou
@time:2019/7/3 16:52
"""

from tools.get_data import GetExcelData
from base.runmethod import RunMethod
from tools.common_util import CommonUtil
from config.config import EnvConf


class CaseData:
    def __init__(self, filename=None):
        self.exceldata = GetExcelData(filename)
        self.casenums = self.exceldata.get_case_lines()

    def get_testcase_data(self):
        test_data = {
            'parameterize': []
        }
        case_data_ids = []
        for case in range(1, self.casenums + 1):
            if self.exceldata.get_is_auto_run(case):
                case_data_json = {
                    'request-data': {},
                    'response-data': {}
                }
                case_method = self.exceldata.get_request_method(case)
                data_url = self.exceldata.get_request_url(case)
                case_url = f"http://{EnvConf.host}:{EnvConf.port}" + data_url
                case_data = self.exceldata.get_request_data(case)
                case_statuscode = self.exceldata.get_response_statuscode(case)
                case_checkpoint = self.exceldata.get_checkpoints(case)
                case_validate = self.exceldata.get_validate(case)
                case_uniqueid = self.exceldata.get_caseuniqueid(case)
                case_data_json['request-data']['url'] = case_url
                case_data_json['request-data']['data'] = case_data
                case_data_json['request-data']['method'] = case_method
                case_data_json['response-data']['statuscode'] = case_statuscode
                case_data_json['response-data']['checkpoint'] = case_checkpoint
                case_data_json['response-data']['validate'] = case_validate
                case_data_ids.append(case_uniqueid)
                test_data['parameterize'].append(case_data_json)
        return test_data, case_data_ids


class BaseTest:
    runmethod = RunMethod()
    validate = CommonUtil()


if __name__ == '__main__':
    testdata = CaseData('test.xlsx')
    # print(testdata.get_testcase_data())
    testdata.get_testcase_data()
    # data, ids = testdata.get_testcase_data()
    # print(data, ids)
