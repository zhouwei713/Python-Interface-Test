# coding = utf-8
"""
@author: zhou
@time:2019/7/4 17:39
"""


from config.config import UserInfo, EnvConf
import requests


def adminlogin():
    url = f"http://{EnvConf.host}:{EnvConf.port}/api/user-management/tokens"
    data = UserInfo.admininfo
    resp = requests.post(url=url, json=data)

    try:
        token = f"Bearer {resp.json()['data']['access_token']}"
    except:
        raise

    return token


def commonlogin():
    url = f"http://{EnvConf.host}:{EnvConf.port}/api/user-management/tokens"
    data = UserInfo.commoninfo
    resp = requests.post(url=url, json=data)

    try:
        token = f"Bearer {resp.json()['data']['access_token']}"
    except:
        raise

    return token
