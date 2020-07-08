import configparser
import os
import os
import sys
base_path = os.path.dirname(os.getcwd())

# file_path ='D:\PythonWorkSpace\interfacetest\Config\server.ini'
# cf = configparser.ConfigParser()
# cf.read(file_path)
# data = cf.get('server','host')
# print(data)

class HandleInit():


    def load_ini(self):
        file_path = base_path+'\Config\server.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf

    def get_value(self,key,attr=None):
        '''
        获取ini里对应字段的value
        :return:
        '''
        if attr == None:
            attr = 'server'
        cf = self.load_ini()
        try:
            #print(attr, key)
            data = cf.get(attr,key)
        except:
            print('没有获取到值')
            data = None
        finally:
            return data
handler_ini = HandleInit()

