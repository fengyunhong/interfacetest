import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    data = {
        "username":"hxd",
        "password":"12345"
    }
    return data

@app.route('/passport/user/login',methods=["GET"])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username and password :
        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登录成功",
            "info":"just a test"
        },ensure_ascii=False)
    else:
        data =json.dumps({
            "message":"参数错误，登录失败",
        },ensure_ascii=False)
    return data

@app.route('/passport/user/post_login',methods=["POST"])
def post_login():
    method = request.method
    if method == 'POST':
        username = request.args.get('username')
        password = request.args.get('password')
        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登录成功",
            "info":"just a test"
        },ensure_ascii=False)
    else:
        data =json.dumps({
            "message":"请求方法错误",
        },ensure_ascii=False)
    return data




if __name__ == '__main__':
    app.run()
