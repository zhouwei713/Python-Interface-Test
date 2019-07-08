# coding = utf-8
"""
@author: zhou
@time:2019/7/3 16:52
"""

from tools.get_data import GetExcelData
from base.runmethod import RunMethod
from tools.common_util import CommonUtil
from config.config import EnvConf, Header
import json
from tools.excel_operation import OperationExcel
from tools.common_util import adminlogin, commonlogin


class CaseDataAllSheets:
    def __init__(self, filename=None):
        self.filename = filename
        self.opera_excel = OperationExcel(filename)
        self.sheet_nums = self.opera_excel.get_sheets()

    def get_all_sheets_data(self):
        total_data = {
            "sheet-data": [],
            'case_data_ids': []
        }
        for i in range(len(self.sheet_nums)):
            data = {}
            sheet_name = self.opera_excel.get_sheet_name()[i]
            casedata = CaseData(filename=self.filename, sheet_id=i)
            test_data, case_data_ids = casedata.get_testcase_data()
            data[sheet_name] = test_data
            total_data['sheet-data'].append(data)
            total_data['case_data_ids'].append(case_data_ids)
        return total_data


class CaseData:
    def __init__(self, filename=None, sheet_id=0):
        self.exceldata = GetExcelData(filename, sheet_id)
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
                if case_data != '':
                    try:
                        case_data = json.loads(case_data)
                    except:
                        raise
                case_header = self.exceldata.get_header(case)
                if case_header == '':
                    case_header = Header.headers
                else:
                    try:
                        case_header = json.loads(case_header)
                    except:
                        raise
                case_statuscode = self.exceldata.get_response_statuscode(case)
                case_checkpoint = self.exceldata.get_checkpoints(case)
                case_validate = self.exceldata.get_validate(case)
                case_uniqueid = self.exceldata.get_caseuniqueid(case)
                print(case_uniqueid)
                print(type(case_uniqueid))
                case_authtype = self.exceldata.get_authtype(case)
                if case_authtype == 0:
                    token = adminlogin()
                    case_header['authorization'] = token
                elif case_authtype == 1:
                    token = commonlogin()
                    case_header['authorization'] = token
                else:
                    pass
                case_data_json['request-data']['url'] = case_url
                case_data_json['request-data']['data'] = case_data
                case_data_json['request-data']['header'] = case_header
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
    # mydata = CaseDataAllSheets('test.xlsx')
    # print(mydata.get_all_sheets_data())
    # print(len(mydata.get_all_sheets_data()['sheet-data']))
    testdata = CaseData('test.xlsx', 1)
    # # print(testdata.get_testcase_data())
    # # testdata.get_testcase_data()
    data, ids = testdata.get_testcase_data()
    print(data, ids)
