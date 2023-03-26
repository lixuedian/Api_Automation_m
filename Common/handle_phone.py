"""
1、随机生成11位手机号  前3位+8位
2、进行数据校验
"""

import random

from Common.Mysql_operate import MysqlDb
from Common.handle_requests import send_requests
from Config.Config import Config

prefix = [ 133,149,153,173,177,180,181,189,199,
           130,131,132,145,155,156,166,171,175,176,185,186,166,
           134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198
]


def get_new_phone():
    db = MysqlDb(Config().mysql_conf('mysql'))
    while True:
        # 1生成
        phone = __generator_phone()
        # 2校验，有
        count = db.get_count('select * from user_base_info where mobile="{}"'.format(phone))
        if count == 0:  # 如果手机号码没有在数据库查到。表示是未注册的号码。
            return phone


def get_new_email():
    db = MysqlDb(Config().mysql_conf('mysql'))
    while True:
        # 1生成
        phone = __generator_phone()
        email = '{}@163.com'.format(phone)
        count = db.get_count('select * from user_base_info where email="{}"'.format(email))
        # 2校验，有
        if count == 0:  # 如果手机号码没有在数据库查到。表示是未注册的号码。
            return email


def get_new_bank_card():
    db = MysqlDb(Config().mysql_conf('mysql'))
    while True:
        # 1生成
        bank_card = __generator_bank_card()
        # 2校验，有
        count = db.get_count('select * from otc_pay_type where bank_card="{}"'.format(bank_card))
        if count == 0:  # 如果手机号码没有在数据库查到。表示是未注册的号码。
            return bank_card


# def get_old_phone():
#     """
#     从配置文件获取指定的用户名和密码
#     确保此帐号，在系统当中是注册了的。
#     返回：用户名和密码。
#     """
#     from Common.handle_config import conf
#     user = conf.get("general_user", "old_phone")
#     passwd = conf.get("general_user", "passwd")
#     # 如果数据库查找到user，就直接返回。如果没有，则调用注册接口注册一个。
#     # 不管注册与否，直接调用注册接口。
#     # send_requests("POST", "member/register", {"mobile_phone": user, "pwd": passwd})
#     return user, passwd


# def get_old_email():
#     """
#     从配置文件获取指定的用户名和密码
#     确保此帐号，在系统当中是注册了的。
#     返回：email和密码。
#     """
#     from Common.handle_config import conf
#     email = conf.get("general_user", "old_email")
#     passwd = conf.get("general_user", "passwd")
#     # 如果数据库查找到user，就直接返回。如果没有，则调用注册接口注册一个。
#     # 不管注册与否，直接调用注册接口。
#     # send_requests("POST", "member/register", {"mobile_phone": user, "pwd": passwd})
#     return email, passwd


def __generator_phone():
    index = random.randint(0, len(prefix) - 1)
    phone = str(prefix[index])  # 前3位
    for _ in range(0, 5):  # 生成后8位
        phone += str(random.randint(0, 9))
    return phone


def __generator_bank_card():
    index = random.randint(0, len(prefix) - 1)
    bank_card = str(prefix[index])  # 前3位
    for _ in range(0, 9):  # 生成后8位
        bank_card += str(random.randint(0, 10))
    return bank_card


# print(get_new_phone())
# print(get_new_email())
# print(get_old_phone())
# print(get_old_email())
# print(get_new_bank_card())
# print(__generator_phone())