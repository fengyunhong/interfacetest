import os
import sys
base_path = os.getcwd()[0:-4]
sys.path.append(base_path)
#from Util.handle_excel import
from Util.handle_excel import excel_data
from jsonpath_rw import parse
import json

def split_data(data):
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data


def depend_data(data):
    '''
    获取依赖数据的所有data
    :param data:
    :return:
    '''
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number,14)
    return data


def get_depend_data(res_data,key):
    '''
    获取依赖字段的值
    :param res_data:
    :param key:
    :return:
    '''
    #print("----111",res_data)
    #print("----111",key)
    res_data=str(res_data)
    res_data=json.loads(res_data)
    json_exe = parse(key)
    result = json_exe.find(res_data)
    #print("----111",result)
    return [math.value for math in result][0]


def get_data(data):
    '''
    获取依赖数据
    :param data:
    :return:
    '''
    res_data = depend_data(data)
    rule_data =split_data(data)[1]
    #print(rule_data,res_data)
    return get_depend_data(res_data,rule_data)



if __name__ == '__main__':
    #data = depend_data('imooc_005>data:banner:id')
    #print(data)
    data = {
            "status":0,
            "data":{
                "banner":[
                    {
                        "id":1709,
                        "type":6,
                        "type_id":354,
                        "name":"Node.js开发仿知乎服务端 深入理解RESTful API",
                        "pic":"http://szimg.mukewang.com/5d0ed27508f7d96909000300.jpg",
                        "links":""
                    }
                ]
        }}
    key='data.banner.[0].id'
    print(get_depend_data(data,key))