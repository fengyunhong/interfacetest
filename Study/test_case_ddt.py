import os
base_path = os.getcwd()[0:-5:]
import ddt
import unittest
from Util.handle_excel import excel_data
data = excel_data.get_excel_data()
print(data)
data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
@ddt.ddt
class TestCase01(unittest.TestCase):


    def setUp(self):
        print('case开始执行')

    def tearDown(self):
        print('case执行结束')

    @ddt.data(*data)
    def test_01(self,data1):
        casename,casenum,isrun,method,cookie=data1
        print('this is a test', casename,casenum,isrun,method,cookie)

if __name__ == '__main__':
        unittest.main()