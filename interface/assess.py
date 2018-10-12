'''
created on 20181012
@author: zhou
'''

def Assess_in(except_data, result_data):
    if len(except_data.split('=')) > 1:
        data = dict([except_data.split('=')])
        result = result_data['result']['code']
        if str(result) == data['code']:
            return {'code': 0, 'result': 'PASS'}
        else:
            return {'code': 1, 'result': 'FAIL'}
    else:
        print('Put except value please!')
        return {'code': 2, 'result': 'Put except value please'}

