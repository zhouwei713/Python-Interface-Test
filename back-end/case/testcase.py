'''
created on 20181009

@author: zhou
'''

from interface.test_API import TestApi
from interface.get_excel import data
import os
from config.config import error_try_num
from interface.assess import Assess_in

file = os.getcwd() + '/data/case.xlsx'

testid, testname, testkey, testparam, testurl, testmode, testexcept = data(file)


def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_weizhi = 0
    list_exption = 0
    error_num = 0
    for i in range(len(testurl)):
        # while error_num <= error_try_num + 1:
            api = TestApi(url=testurl[i], mode=testmode[i], key=testkey[i])
            apijson = api.getJson()
            if apijson['code'] == 0:
                print('url: %s, result: %s, except: %s' %(testurl[i], apijson, testexcept[i]))
                assess_res = Assess_in(testexcept[i], apijson)
                # print(assess_res)
                if assess_res['code'] == 0:
                    print('PASS')
                    list_json.append(apijson['result'])
                    listrelust.append('pass')
                    list_pass += 1
                    error_num = 0
                    continue
                elif assess_res == 1:
                    print('Need retry')
                    if error_num <= error_try_num:
                        error_num += 1
                        print('Retry...')
                    else:
                        print('Finish retry, check result')
                        error_num = 0
                        list_fail += 1
                        listrelust.append('fail')
                        list_json.append(apijson['result'])
                        break
                elif assess_res == 2:
                    print('No except value input')
                else:
                    print('Unknown Error')
                    if error_num < error_try_num:
                        error_num += 1
                        print('Retry...')
                    else:
                        print('Finish retry, check result')
                        error_num = 0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(apijson['result'])
                        break
            else:
                print('Request to url fail!')
    return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi
