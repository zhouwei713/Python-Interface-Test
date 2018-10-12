'''
created on 20181012
@author: zhou
'''

import requests, json

class requ():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
    def get(self, url, params):
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            print('get error: %s' %e )
            return {'code': 1, 'result': 'get error: %s' %e}
