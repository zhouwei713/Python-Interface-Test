# coding = utf-8
"""
@author: zhou
@time:2019/7/3 17:12
"""


import pytest
import requests
from config.config import EnvConf


@pytest.fixture(scope='session')
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


@pytest.fixture(scope='session')
def token_admin():
    url = f"http://{EnvConf.host}:{EnvConf.port}/api/user-management/tokens"
    data = {
        "username": "administrator",
        "password": "Abba123456@"
    }
    resp = requests.post(url=url, json=data)
    # print(resp.json())

    token = f"Bearer {resp.json()['data']['token']}"
    return token


def pytest_addoption(parser):
    parser.addoption("--casefile", action="store", help="passing the testcase file")


@pytest.fixture
def casefile(request):
    if request.config.getoption('--casefile'):
        return request.config.getoption('--casefile')


