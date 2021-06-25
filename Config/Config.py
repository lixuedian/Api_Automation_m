# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Config.py
# 开发工具 ： PyCharm
from configparser import ConfigParser
from Common import Log, GToken as Gt
import os

TITLE_TOKEN = 'parameter'


def get_token():
    return Gt.get_value('')


class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"
    TITLE_HOST = "test_host"
    TITLE_TOKEN = 'parameter'
    TITLE_TOKEN_ZT = 'Trading'
    TITLE_TOKEN_ZT_HT = 'Integrated'

    VALUE_TEST_04_UNIFIDE_URL = "test04_unified_url"
    VALUE_TEST_SHIJUAN_URL = "test_shijian_url"
    VALUE_TEST_Position_URL = "test_position_url"
    VALUE_TEST_express_URL = "test_express_url"
    VALUE_TEST_04_user_URL = 'user_url'
    # token
    VALUE_TEST_Token = 'token'
    VALUE_test_mp_url = 'test_mp_url'


    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"
    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        # self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        # self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        # self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        # self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        # self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        # self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
        #
        # self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
        # self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        # self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        # self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        # self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        # self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)

        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)
        self.test04_unified_url = self.get_conf(Config.TITLE_HOST, Config.VALUE_TEST_04_UNIFIDE_URL)
        self.test_shijian_url = self.get_conf(Config.TITLE_HOST, Config.VALUE_TEST_SHIJUAN_URL)
        self.test_Position_url = self.get_conf(Config.TITLE_HOST, Config.VALUE_TEST_Position_URL)
        self.test_express_url = self.get_conf(Config.TITLE_HOST, Config.VALUE_TEST_express_URL)
        self.test_user_url = self.get_conf(Config.TITLE_HOST, Config.VALUE_TEST_04_user_URL)

        self.token = self.get_conf(Config.TITLE_TOKEN, Config.VALUE_TEST_Token)
        # 综合后台用户token
        self.h_token = self.get_conf(Config.TITLE_TOKEN_ZT_HT, Config.VALUE_TEST_Token)
        # 交易中台用户token
        self.token_zt = self.get_conf(Config.TITLE_TOKEN_ZT, Config.VALUE_TEST_Token)
        self.test_mp_url = self.get_conf(Config.TITLE_TOKEN_ZT, Config.VALUE_test_mp_url)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        res = self.config.get(title, value)

        # print('========', res)
        return res

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        if 'token' == value:
            Gt.set_token(text)
        if 'uuid' == value:
            Gt.set_uuid(text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def write_configuration(self, parameter, token):
        # 写入配置文件
        self.set_conf(parameter, 'token', token)
        print('tokoen写入配置文件成功')
        Log.MyLog().info('写入配置文件成功，token ={}'.format(self.get_conf(parameter, 'token')))



