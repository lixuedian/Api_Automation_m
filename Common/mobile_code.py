"""
获取短信验证码的接口
"""
import sys

import flask
import json
from flask import request
from Common.handle_data import EnvData
from Common.handle_extract_data_from_response import db_code

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式


@server.route('/mobile_code', methods=['get', 'post'])
def mobile_code():
    """
    获取短信验证码接口
    :return:
    """
    # 获取通过url请求传参的数据
    num = request.values.get('code')
    # 获取url请求传的密码，明文
    iphone = request.values.get('mobile')
    email = request.values.get('email')
    # 判断用户名、密码都不为空
    msg = "查询短信验证码" \
          "num=0, 注册验证码" \
          "num=1, 登录验证码" \
          "num=2, 提现验证码" \
          "num=3， 修改登录密码" \
          "num=4， 修改交易密码" \
          "num=5， 用户账号提醒：【Bitvito】您的USDT合约账户风险度已超过90%（达到100%将进入爆仓流程）,请注意及时调整交易策略以避免发生强制平仓" \
          "num=11， 【Bitvito】您的$coin$币本位合约，$quantity$仓位已接近强平价格，请注意及时调整交易策略以避免发生强制平仓。" \
          "num=6，【Bitvito】因行情剧烈波动，您的USDT合约账户因资金不足，风险度已达到100%，已被执行强平委托。" \
          "num=12， 【Bitvito】因行情剧烈波动，您的$coin$币本位合约$quantity$，已被执行强平委托。" \
          "num=7，邮箱验证码" \
          "num=13，邮箱登录验证码" \
          "num=8，绑定邮箱" \
          "num=9 绑定手机验证码" \
          "num=10 您正在进行安全验证,您的验证码为" \
          "num=14 修改邮箱密码"
    if iphone and num:
        db_code('mobile_code', num, iphone)
        b = EnvData.__dict__
        b = b['mobile_code']
        if b == '':
            res = {'code': 200, 'message': '验证码不存在，请重新获取'}
            return json.dumps(res, ensure_ascii=False)
        else:
            res = {'code': 200, 'mobile_code': b, 'message': '获取验证码成功'}
            return json.dumps(res, ensure_ascii=False)  # 将字典转换字符串
    elif email and num:
        db_code('email_code', num, email)
        b = EnvData.__dict__
        b = b['email_code']
        if b == '':
            res = {'code': 200, 'message': '验证码不存在，请重新获取'}
            return json.dumps(res, ensure_ascii=False)
        else:
            res = {'code': 200, 'email_code': b, 'message': '获取验证码成功'}
            return json.dumps(res, ensure_ascii=False)  # 将字典转换字符串
    else:
        res = {'code': 10001, 'data': msg, 'message': '参数不能为空！'}
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8881, host='192.168.3.77')
