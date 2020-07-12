
from deepdiff import DeepDiff
from Util.handle_json import get_value
import os
base_path =os.path.dirname(os.getcwd())

#print(get_value('api3/getbanneradvertver2',file_name='\Config\code_message.json'))


def  handle_result(url,code):
    data = get_value(url,file_name=r'/Config/code_message.json')
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None



def  get_result_json(url,status):
    data = get_value(url,file_name=r'/Config/result.json')
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None




def handle_result_json(dict1,dict2):
    '''
    校验格式
    :return:
    '''
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        #print(cmp_dict)
        if cmp_dict.get('dictionary_item_added'):
            return False
        else:
            return True
    return False
if __name__ == '__main__':
    data1={'status': 0, 'data': '', 'errorCode': 1002, 'errorDesc': '成功', 'timestamp': 0}
    data2={'status': 1, 'data': [], 'errorCode': 1006, 'errorDesc': 'token error', 'timestamp': 1594128575884}
    print(type(data1))
    print(type(data2))
    print(handle_result_json(data1,data2))