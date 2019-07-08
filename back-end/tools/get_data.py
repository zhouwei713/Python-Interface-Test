# coding = utf-8
"""
@author: zhou
@time:2019/7/3 11:40
"""


from tools.excel_operation import OperationExcel
from tools.operate_data import OperateExcelData


class GetExcelData(object):
    def __init__(self, filename=None, sheet_id=0):
        self.operate_excel = OperationExcel(filename, sheet_id)
        self.operate_data = OperateExcelData()

    # 获取 sheet 个数
    def get_sheets(self):
        sheet_num = self.operate_excel.get_sheets()
        return len(sheet_num)

    # 获取 excel 行数，即用例个数
    def get_case_lines(self):
        return self.operate_excel.get_lines()

    # 获取是否执行
    def get_is_auto_run(self, row):
        auto_flag = False
        col = int(self.operate_data.get_is_auto_run())
        run_model = self.operate_excel.get_cell_value(row, col)
        if run_model == 1:
            auto_flag = True
        else:
            auto_flag = False
        return auto_flag

    # 获取请求方式
    def get_request_method(self, row):
        col = int(self.operate_data.get_method())
        request_method = self.operate_excel.get_cell_value(row, col)
        return request_method

    # 获取 url
    def get_request_url(self, row):
        col = int(self.operate_data.get_url())
        url = self.operate_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(self.operate_data.get_data())
        data = self.operate_excel.get_cell_value(row, col)
        return data

    # 获取 status code
    def get_response_statuscode(self, row):
        col = int(self.operate_data.get_statuscode())
        statuscode = self.operate_excel.get_cell_value(row, col)
        return statuscode

    # 获取 checkpoints
    def get_checkpoints(self, row):
        col = int(self.operate_data.get_checkpoints())
        checkpoints = self.operate_excel.get_cell_value(row, col)
        return checkpoints

    # 获取 validate
    def get_validate(self, row):
        col = int(self.operate_data.get_validate())
        validate = self.operate_excel.get_cell_value(row, col)
        return validate

    # 获取测试用例唯一 ID
    def get_caseuniqueid(self, row):
        col = int(self.operate_data.get_caseuniqueid())
        caseuniqueid = self.operate_excel.get_cell_value(row, col)
        if isinstance(caseuniqueid, float):
            caseuniqueid = int(caseuniqueid)
        return str(caseuniqueid)

    # 获取 header 信息
    def get_header(self, row):
        col = int(self.operate_data.get_header())
        header = self.operate_excel.get_cell_value(row, col)
        return header

    # 获取是否需要鉴权信息
    def get_authtype(self, row):
        col = int(self.operate_data.get_authtype())
        authtype = self.operate_excel.get_cell_value(row, col)
        return authtype


if __name__ == '__main__':
    data = GetExcelData()
    print(data.get_case_lines())
    print(data.get_sheets())
