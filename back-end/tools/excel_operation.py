# coding = utf-8
"""
@author: zhou
@time:2019/7/3 10:42
"""


import xlrd
from config.config import PROJECT_PATH


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=0):
        if file_name:
            self.file_name = PROJECT_PATH + '/data/' + file_name
            self.sheet_id = sheet_id
        else:
            try:
                self.file_name = PROJECT_PATH + '/data/case.xlsx'
                self.sheet_id = 0
            except FileExistsError:
                raise FileExistsError("the default testcase file not found")
        self.book = self.get_book()
        self.data = self.get_data()

    # 获取工作簿
    def get_book(self):
        book = xlrd.open_workbook(self.file_name)
        return book

    # 获取 sheets 的内容
    def get_data(self):
        book = self.book
        tables = book.sheets()[self.sheet_id]
        return tables

    # 获取所有 sheet 的名字
    def get_sheet_name(self):
        book = self.book
        return book.sheet_names()

    # 获取所有 sheets
    def get_sheets(self):
        book = self.book
        sheets = book.sheets()
        return sheets

    # 获取某个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        case_rows = tables.nrows - 1
        return case_rows

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    # 获取某一行的内容
    def get_rows_data(self, row_id=None):
        if row_id is not None:
            rows = self.data.row_values(row_id)
        else:
            rows = self.data.row_values(0)
        return rows

    # 获取某个 caseid 对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1


if __name__ == '__main__':
    import os
    print(os.getcwd())
    opers = OperationExcel()
    print(opers.get_cell_value(1, 1))
    print(opers.get_cols_data(1))
    print(opers.get_rows_data(3))
    print(opers.get_rows_data(2))
    print(opers.get_sheet_name()[1])
    print(opers.get_sheets())
    print(opers.get_sheets()[1].cell_value(0, 0))

