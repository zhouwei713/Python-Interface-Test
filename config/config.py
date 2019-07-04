"""
created on 20181012
@author: zhou
"""

error_try_num = 3


PROJECT_PATH = r"C:/\Work/\code/\Python/\Python-test-platform/\Python-Interface-Test/"


class ExcelConfData:
    caseid = '0'
    casename = '1'
    caselevel = '2'
    preconditions = '3'
    testcontent = '4'
    expect = '5'
    casecategory = '6'
    automated = '7'  # 1 是自动运行， 2 是非自动运行
    caseuniqueid = '1'  # 8
    method = '9'
    url = '10'
    data = '11'
    statuscode = '12'
    checkpoints = '13'
    validate = '14'
    result = '15'


class JsonConfData:
    pass


class DBConnection:
    pass


class EnvConf:
    host = '10.150.8.143'
    port = '10000'
