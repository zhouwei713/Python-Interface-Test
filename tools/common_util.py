# coding = utf-8
"""
@author: zhou
@time:2019/7/3 13:53
"""


import json
import operator


class CommonUtil(object):
    def is_contain(self, str1, str2):
        """
        :param str1: 原始字符串
        :param str2: 被查找的字符串
        :return: True or False
        """
        flag = None
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, d1, d2):
        if isinstance(d1, str):
            d1 = json.loads(d1)
        if isinstance(d2, str):
            d2 = json.loads(d2)
        return operator.eq(d1, d2)




