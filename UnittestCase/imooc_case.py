from datetime import datetime

import unittest
from Base.base_request import request
import HTMLTestRunner
host = 'https://coding.imooc.com/'
import os
base_path = os.getcwd()

class ImoocCase(unittest.TestCase):
   def test_ajaxins(self):
       url = host+'class/ajaxconsultsearch?'
       data = {
           "cid":"418",
           "page":"1",
           "pagesize":"6",
           "words":""
       }
       res = request.run_main('get',url,data)
       self.assertEqual(res['msg'],'成功')

   def test_total(self):
       url = host+'class/ajaxconsultsearch?'
       data = {
           "cid":"418",
           "page":"1",
           "pagesize":"6",
           "words":""
       }
       res = request.run_main('get',url,data)
       self.assertEqual(res['msg'],'成功')

   def test_result(self):
       url = host + 'class/ajaxconsultsearch?'
       data = {
           "cid": "418",
           "page": "1",
           "pagesize": "6",
           "words": ""
       }
       res = request.run_main('get', url, data)
       self.assertEqual(res['result'], 1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_ajaxins'))
    suite.addTest(ImoocCase('test_total'))
    suite.addTest(ImoocCase('test_result'))
    temppath='D:\PythonWorkSpace\interfacetest\\report'
    date=datetime.today().date()
    print(date)
    filepath=temppath+'\\'+str(date)+'report.html'
    print(filepath)
    print('a1')
    with open(filepath,'wb') as f :
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'搜索功能测试报告',
            description=u'用例执行情况：')
        runner.run(suite)
    f.close()
    print('a')