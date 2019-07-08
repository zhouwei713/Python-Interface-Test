# coding = utf-8
"""
@author: zhou
@time:2019/7/3 10:32
"""

from unittest.mock import patch
from unittest import mock


def mock_test(mock_method, request_data, url, method, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res

