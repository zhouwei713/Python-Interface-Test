'''
created on 20181012
@author: zhou
'''

from .test_request import requ

request = requ()


class TestApi(object):
    def __init__(self, url, mode, key):
        self.url = url
        self.mode = mode
        self.key = key

    def testapi(self):
        if self.mode == 'GET':
            self.param = {'key': self.key}
            self.response = request.get(url=self.url, params=self.param)
        elif self.mode == 'POST':
            pass
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data


