import requests
import unittest
from Base.base_request import request
class TestCase01(unittest.TestCase):



    def setUp(self) -> None:
        print("开始执行case")

    def tearDown(self) -> None:
        print("case执行结束")

    @classmethod
    def setUpClass(cls) -> None:
        print("开始执行类方法case")

    @classmethod
    def tearDownClass(cls) -> None:
        print("结束执行类方法case")

    def test_03(self):
        print("case03")

    def test_01(self):
        print("case01")

    def test_02(self):
        print("case02")

    def test_04(self):
        print("case04")

    def test_05(self):
        data={
            'username':"123",
            "password":"3213"
        }
        url = 'http://www.imooc.com/article/26870'
        res=request.run_main('get',url=url,data=data)
        print(res)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCase01('test_05'))
    suite.addTest(TestCase01('test_04'))
    suite.addTest(TestCase01('test_03'))
    suite.addTest(TestCase01('test_02'))
    #lists = [TestCase01('test_05'),TestCase01('test_04'),TestCase01('test_03')]
   # suite.addTests(lists)
    runner = unittest.TextTestRunner()
    runner.run(suite)

