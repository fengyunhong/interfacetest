import json
from Util.handle_excel import excel_data
from Base.base_request import request
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.condition_data import get_data
import os
import sys
base_path = os.path.dirname(os.getcwd())
print(base_path)
class RunMain():
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            cookie=None
            get_cookie=None
            header=None
            depend_data=None
            data = excel_data.get_rows_value(i+2)
            ''' 将每行数据取到，分别取每个字段的值
            ['imooc_001', '获取广告位', 'yes', None, 'api3/getbanneradvertver2', 'post', '{"username":"111111"}', 'yes', 'mec', None, None]
            '''
            is_run = data[2]

            if is_run == 'yes':

                data1=json.loads(data[7])
                is_depend=data[3]

                if is_depend:
                    '''
                      获取依赖数据
                    '''
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = depend_data


                method = data[6]
                url = data[5]
                #data1 = data[7]
                is_header = data[9]
                expect_method = data[10]
                expect_result = data[11]
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie={"is_cookie":"app"}
                if is_header == 'yes':
                    header = get_header()
                print(data[13])
                res =request.run_main(method,url,data1,cookie,get_cookie,header)
                code=str(res['errorCode'])
                message=res['errorDesc']
                if expect_method == 'mec':
                    config_message = handle_result(url,code)
                    if message == config_message:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if expect_method == 'errorcode':
                    if expect_result == code:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i + 2, 13, '失败')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))
                if expect_method == 'json':
                    if code == 1000:
                        status_str='sucess'
                    else:
                        status_str='error'
                    expect_result = get_result_json(url,status_str)
                    result = handle_result_json(res,expect_result)
                    if  result:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i + 2, 13, '失败')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))
if __name__ == '__main__':
    run = RunMain()
    run.run_case()