import os
base_path = os.getcwd()[0:-4:]
from  Util.handle_json import read_json


def get_header():
    data = read_json("/Config/header.json")
    return data


