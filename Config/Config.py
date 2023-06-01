# -*- coding: utf-8 -*-
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Config.py
# 开发工具 ： PyCharm
from configparser import ConfigParser
from Common import Log, GToken as Gt
import os
import Common.Read_data
from Common.Delete import deletes_file

TITLE_TOKEN = 'parameter'
config_ini = 'config_test.ini'  # 指定环境配置文件


def get_token():
    return Gt.get_value('')


class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"
    TITLE_HOST = "server"
    TITLE_TOKEN = 'parameter'
    TITLE_TOKEN_ZT = 'Trading'
    TITLE_TOKEN_ZT_HT = 'Integrated'
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
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_ini)
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'
        self.allure_report = Config.path_dir+'/allure-report'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        # self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        # self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        # self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        # self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
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
        # 交易员请求host
        self.cas_url = self.get_conf(Config.TITLE_HOST, 'cas_url')
        self.home_url = self.get_conf(Config.TITLE_HOST, 'home_url')
        self.finance_url = self.get_conf(Config.TITLE_HOST, 'finance_url')
        self.wlms_url = self.get_conf(Config.TITLE_HOST, 'wlms_url')

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
        if 'cookies' == value:
            Gt.set_cookies(text)
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

    def write_configuration(self, parameter='parameter', token=None, uuid=None, cookies=None):
        # 写入配置文件
        if token:
            self.set_conf(parameter, 'token', token)
            Log.MyLog().info('写入配置文件成功，token ={}'.format(token))
        if uuid:
            self.set_conf(parameter, 'uuid', uuid)
            Log.MyLog().info('写入配置文件成功，uuid ={}'.format(uuid))
        if cookies:
            self.set_conf(parameter, 'Cookie', cookies)
            Log.MyLog().info('写入配置文件成功，uuid ={}'.format(uuid))
        # print('token写入配置文件成功')

    def delete_file(self):
        # 清空allure文件
        deletes_file(self.xml_report_path)
        deletes_file(self.html_report_path)
        deletes_file(self.allure_report)

    # 读取配置参数
    def mysql_conf(self, conf):
        data = Common.Read_data.data.load_ini(self.conf_path)[f'{conf}']
        db_conf = {
            "host": data["mysql_host"],
            "port": int(data["mysql_port"]),
            "user": data["mysql_user"],
            "password": data["mysql_passwd"],
            "db": data["mysql_db"]
        }
        return db_conf


# print(Config().get_conf("data", "old_phone"))
