from datetime import datetime
import os
base_path = os.path.dirname(os.getcwd())
import ddt
import unittest
import json
from Util.handle_excel import excel_data
from Base.base_request import request
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.condition_data import get_data
import HTMLTestRunner

data = excel_data.get_excel_data()

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self,data):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            is_run = data[2]
            case_id = data[0]
            i = excel_data.get_rows_number(case_id)
            if is_run == 'yes':
                is_depend = data[3]
                data1 = json.loads(data[7])
                try:
                    if is_depend:
                        '''
                        获取依赖数据
                        '''
                        depend_key = data[4]
                        depend_data = get_data(is_depend)
                        # print(depend_data)
                        data1[depend_key] = depend_data

                    method = data[6]
                    url = data[5]

                    is_header = data[9]
                    excepect_method = data[10]
                    excepect_result = data[11]
                    cookie_method = data[8]
                    if cookie_method == 'yes':
                        cookie = get_cookie_value('app')
                    if cookie_method == 'write':
                        '''
                        必须是获取到cookie
                        '''
                        get_cookie = {"is_cookie": "app"}
                    if is_header == 'yes':
                        header = get_header()

                    res = request.run_main(method, url, data1, cookie, get_cookie, header)
                    # print(res)
                    code = str(res['errorCode'])
                    message = res['errorDesc']
                    # message+errorcode

                    if excepect_method == 'mec':
                        config_message = handle_result(url, code)
                        '''
                            if message == config_message:
                                excel_data.excel_write_data(i,13,"通过")
                            else:
                                excel_data.excel_write_data(i,13,"失败")
                                excel_data.excel_write_data(i,14,json.dumps(res))
                        '''
                        try:
                            self.assertEqual(message, config_message)
                            excel_data.excel_write_data(i, 13, "通过")
                            excel_data.excel_write_data(i, 14, json.dumps(res))
                        except Exception as e:
                            excel_data.excel_write_data(i, 13, "失败")
                            raise e

                    if excepect_method == 'errorcode':
                        '''
                        if excepect_result == code:
                            excel_data.excel_write_data(i,14,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                        '''
                        try:
                            self.assertEqual(excepect_result, code)
                            excel_data.excel_write_data(i, 13, "通过")
                        except Exception as e:
                            excel_data.excel_write_data(i, 13, "失败")
                            raise e
                    if excepect_method == 'json':

                        if code == 1000:
                            status_str = 'sucess'
                        else:
                            status_str = 'error'
                        excepect_result = get_result_json(url, status_str)
                        result = handle_result_json(res, excepect_result)
                        '''
                        if result:
                            excel_data.excel_write_data(i,13,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))   
                        '''
                        try:
                            self.assertTrue(result)
                            excel_data.excel_write_data(i, 13, "通过")
                        except Exception as e:
                            excel_data.excel_write_data(i, 13, "失败")
                            raise e
                except Exception as e:
                    excel_data.excel_write_data(i, 13, "失败")
                    raise e
if __name__ == '__main__':
    date = datetime.today().date()
    report_path = base_path +'\\report'+ '\\' + str(date) + 'report.html'
    case_path=base_path+'\Run\\'
    discover = unittest.defaultTestLoader.discover(case_path,pattern='run_case*')
    #unittest.TextTestRunner().run(discover)
    with open(report_path,'wb') as f :
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'接口测试报告',
            description=u'用例执行情况：')
        runner.run(discover)
    f.close()

