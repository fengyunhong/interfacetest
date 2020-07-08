import json
import os
import os
import sys
base_path = os.path.dirname(os.getcwd())
#获取到了Util路径，切片截取最后的
#base_path = base_path.replace('\\','/')
#print(base_path)D:\PythonWorkSpace\interfacetest

def read_json(file_name=None):
    if file_name == None:
        file_path =base_path+r'\Config\user_data.json'
    else:
        file_path = base_path + file_name
    with open(file_path,encoding='utf-8') as f:
         data = json.load(f)
    return data


def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)



def write_value(data):
    data_value = json.dumps(data)
    with open(base_path+r"\Config\cookie.json","w") as f:
        f.write(data_value)

if __name__ == '__main__':
    print(base_path)