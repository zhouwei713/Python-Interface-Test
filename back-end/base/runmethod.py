# coding = utf-8
"""
@author: zhou
@time:2019/7/3 10:17
"""


import requests
import json
from base import exceptions
from base import logger


class RunMethod(object):
    def __init__(self):
        self.verify = False
        self.headers = None

    def post_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None, param=None):
        res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header, verify=self.verify, params=param)
        else:
            res = requests.get(url=url, data=data, verify=self.verify, params=param)
        return res.json()

    def del_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.delete(url=url, data=data, headers=header)
        else:
            res = requests.delete(url=url, data=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        elif method == 'GET':
            res = self.get_main(url, data, header)
        else:
            res = self.del_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

    def run(self, test_data):
        logger.log_debug(f"{test_data['test_case_name']}\n")
        try:
            req_kwargs = test_data['requests']
            url = self.compose_url(req_kwargs.pop('url'))
            method = req_kwargs.pop('method')
        except KeyError:
            raise exceptions.ParamsError("URL or METHOD missed!")

        valid_methods = ["GET", "HEAD", "POST", "PUT", "PATCH",
                         "DELETE", "OPTIONS"]

        if method.upper() not in valid_methods:
            err_msg = u"Invalid HTTP method! => {}\n".format(method)
            err_msg += "Available HTTP methods: {}".format(
                "/".join(valid_methods))
            logger.log_error(err_msg)
            raise exceptions.ParamsError(err_msg)

        logger.log_debug("{method} {url}".format(method=method, url=url))
        logger.log_debug("request kwargs(raw):{kwargs}".format(
            kwargs=req_kwargs))

        if method == 'GET':
            resp_obj = requests.request(
                url=url, method=method, verify=self.verify,
                headers=self.headers, params=req_kwargs['json'])
            print(resp_obj.url)
        else:
            resp_obj = requests.request(
                url=url, method=method,  verify=self.verify,
                headers=self.headers, **req_kwargs)
        return resp_obj

