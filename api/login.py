# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/4 15:51
@Author  : lixuedian
@FileName: login.py
"""
import json

import requests

from Common.Methodes import Notify
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
        # header = GetTicket.header(body)
        url = 'https://www.baidu.com/sugrec?&prod=pc_his&from=pc_web&json=1&sid=38185_36551_38406_38106_38358_38400_38468_38172_38289_38245_36804_38262_37919_38382_37900_26350_38283_37881&hisdata=%5B%7B%22time%22%3A1670424359%2C%22kw%22%3A%22%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1670465325%2C%22kw%22%3A%22listary%22%7D%2C%7B%22time%22%3A1670477340%2C%22kw%22%3A%22%E4%B8%80%E9%94%AE%E8%BF%98%E5%8E%9F%22%7D%2C%7B%22time%22%3A1670477410%2C%22kw%22%3A%22win11%20%E4%B8%80%E9%94%AE%E8%BF%98%E5%8E%9F%22%7D%2C%7B%22time%22%3A1670550820%2C%22kw%22%3A%22%E8%81%94%E6%83%B3%E5%BC%95%E6%93%8E%E6%9C%8D%E5%8A%A1%22%7D%5D&_t=1679843584352&req=2&sc=eb&csor=0'
        response = requests.get(url=url + api, headers={})
        return response

        # response = requests.post(url=url + api, headers={}, data=body)
        # response = response.cookies
        # cookies = requests.utils.dict_from_cookiejar(response)
        # return cookies

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
        header = {'cookies': Login.login()}
        response = requests.post(url=url + api, headers=header, data=body)
        if response.status_code == 200:
            response = response.cookies
            cookies = requests.utils.dict_from_cookiejar(response)
            Config().write_configuration(cookies=cookies)
            return cookies
        elif response.status_code == 401:
            pass

