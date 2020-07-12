import json
import requests
from Util.handle_ini import handler_ini
from Util.handle_cookie import get_cookie_value,write_cookie
class BaseRequest:



    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        'send post '
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])

        res = response.text
        return res

    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        'send get '
        response = requests.get(url=url, data=data, cookies=cookie,headers=header)
        if get_cookie != None:
            res = response.cookies
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])

        res = response.text
        return res


    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):
        '执行方法  传递参数method url data'
        #return get_value(url)
        base_url = handler_ini.get_value('host')
        if 'http://' not in url:
            url = base_url+url
        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)
        try:
            res = json.loads(res)
        except:
            '若返回的res不是json，则会解析失败，返回test，若是json则返回json'
            print('json解析失败,返回网页文本')
        return  res
request = BaseRequest()
