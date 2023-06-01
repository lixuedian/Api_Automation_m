# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/4 15:51
@Author  : lixuedian
@FileName: login.py
"""
import json

import requests

from Common.Methodes import Notify
from Common.signature import value_list
from Config.Config import Config


class Login:

    # 获取cookies
    @staticmethod
    def login(**kwargs):
        """
         :param kwargs: 其他参数
         :return: json格式请求结果

         """
        url = Config().cas_url
        api = f'/login'
        body = {
            "username": 'lixd5',
            "password": 'l8mto35nLEbZIPJDrM7jlMOsQ+EsteQKith24kCTWVjO3hskPcF0vLfYq3OAZ22qjy84Qu/6vYXLEOfGdM7moQ==',
            "otpCode": 1
        }
        response = requests.post(url=url + api, headers={}, data=body)
        response = response.cookies
        cookies = requests.utils.dict_from_cookiejar(response)
        cookies = value_list(cookies)
        config = Config()
        config.write_configuration(cookies=cookies)
        return cookies

    # 获取cookies
    @staticmethod
    def ad_login(**kwargs):
        """
         :param kwargs: 其他参数
         :return: json格式请求结果

         """
        url = Config().home_url
        api = f'/proxy/org/zhyLogin/adLogin'
        body = {
        }
        header = {'Cookie': Login.login()}
        response = requests.post(url=url + api, headers=header, data=body)
        if response.status_code == 200:
            response = response.cookies
            cookies = value_list(requests.utils.dict_from_cookiejar(response))
            config = Config()
            config.write_configuration(cookies=cookies)
            return cookies
        elif response.status_code == 401:
            print('登录失效')
            pass

