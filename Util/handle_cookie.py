from Util.handle_json import get_value ,read_json,write_value
import os
base_path = os.getcwd()[0:-4:]

def get_cookie_value(cookie_key):
    data = read_json(r"\Config\cookie.json")
    return data[cookie_key]

def write_cookie(data,cookie_key):
    data1 = read_json(r"\Config\cookie.json")
    data1[cookie_key] = data
    write_value(data1)



if __name__ == '__main__':
    data = {
        "aa":"teststt"
    }
    print(write_cookie(data,"web"))