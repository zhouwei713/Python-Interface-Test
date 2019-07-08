# coding = utf-8
"""
@author: zhou
@time:2019/7/3 11:45
"""


from config.config import ExcelConfData


class OperateExcelData(object):
    def get_caseid(self):
        return ExcelConfData.caseid

    def get_url(self):
        return ExcelConfData.url

    def get_method(self):
        return ExcelConfData.method

    def get_is_auto_run(self):
        return ExcelConfData.automated

    def get_header(self):
        return ExcelConfData.header

    def get_data(self):
        return ExcelConfData.data

    def get_casename(self):
        return ExcelConfData.casename

    def get_statuscode(self):
        return ExcelConfData.statuscode

    def get_checkpoints(self):
        return ExcelConfData.checkpoints

    def get_validate(self):
        return ExcelConfData.validate

    def get_caseuniqueid(self):
        return ExcelConfData.caseuniqueid

    def get_authtype(self):
        return ExcelConfData.authtype


class OperateJsonData(object):
    pass
