from unittest import mock

import requests
import unittest


url = "http://www.imooc.com/login"
data = {
    "username":"huhuhu",
    "password":"123456"
}

def post_request(url,data):
    res = requests.post(url,data=data).json()
    return res

def get_request(url,data):
    res = requests.get(url,params=data).json()
    return res


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        print("testcase开始执行")

    def tearDown(self) -> None:
        print("testcase执行结束")

    def test_01(self):
        url ="http://www.imooc.com/login/register"
        data = {
            "username":"huxiaodong"
        }
        success_test = mock.Mock(return_value=data)
        post_request = success_test
        res = post_request
        self.assertEqual("1122",res())

if __name__ == '__main__':
    unittest.main()