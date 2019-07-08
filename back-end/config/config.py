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
    header = '12'
    statuscode = '13'
    checkpoints = '14'
    validate = '15'
    parameterize = '16'
    result = '17'
    authtype = '18'  # 0:admin, 1:common user, 2:not login


class JsonConfData:
    pass


class DBConnection:
    pass


class EnvConf:
    host = '10.150.8.143'
    port = '10000'


class Header:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


class UserInfo:
    admininfo = {
        "username": "D8jTPGLJR19LJHBAWkTGupXVawQgLjo149JekG873Zg0pY9MBHiBG/EWIxcvw4TNLl+6ym3fEQWIPCR3WnaBavUodAvn6Xcz0HOBjAni8E/UA5k17qZdm/kJ/6SVwppf8koUIjllkKKspAlkmwtgVNnRjhwPB3c0oROmU67/URc=",
        "password": "EqL5QRhwu8ngKOs3TMKZVSKwV1Rt0MX/OzUS5jcfwmGrincWzdp3GuOuB5QYhWe4YYSIAYAWIJIprXmGJRillsKso/tXrfr/xSigMNdGRnDRP7XDiOf1NkFf11+cuav6zzT0+YTXPc6YdvUn/Lco3SNjuQvZbOy5SB9YRnf1ywQ="
    }

    commoninfo = {
        "username": "TLAQbKyoN5TtIAqUnZH9p5N8TC0TCxO72SOFjs5ug6EKuDYigfS6jx1ccCFIfa0wUoSpymn6ZF+JYrSbiH+wrSnRkSVChVZ5wLX/sT7rLVp4z0bxNLBm0fHdqezOczShiE1rW0/kBkedmsfhH6Q9OsCuUOQtXwlbtPIvIfOHQZY=",
        "password": "G8oy789H9ABPQ5LhWGf+kyxKfzR8i7KHvDNcBZtG3aR64RYRE82jAQFX6g2hXK2L680/JYmPO8DLmZRhYVpbzkfiRdWki+odc6QOJlTFLVNYkC6EeTdFG/STMr1vAmk/vt1gy4jWW5gKj53WoKXFuFiLL9MOshQZshHYx8qTopA="
    }
