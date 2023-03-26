# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Hash.py
# 开发工具 ： PyCharm
"""
封装各种加密方法

"""
import base64
import binascii
import hmac
from hashlib import md5
from hashlib import sha1, pbkdf2_hmac
from hashlib import sha256

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Hash import SHA256, SHA512


def my_md5(msg):
    """
    md5 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    hl = md5()
    hl.update(msg.encode('utf-8'))
    return hl.hexdigest()


def my_sha1(msg):
    """
    sha1 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_sha256(msg):
    """
    sha256 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = SHA256.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_sha512(msg):
    """
    sha512 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = SHA512.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_des(msg, key):
    """
    DES 算法加密
    :param msg: 需加密的字符串,长度必须为8的倍数，不足添加'='
    :param key: 8个字符
    :return: 加密后的字符
    """
    de = DES.new(key, DES.MODE_ECB)
    mss = msg + (8 - (len(msg) % 8)) * '='
    text = de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()


def my_aes_encrypt(msg, key, vi):
    """
    AES 算法的加密
    :param msg: 需加密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return: 加密后的字符
    """
    obj = AES.new(key, AES.MODE_CBC, vi)
    txt = obj.encrypt(msg.encode())
    return binascii.b2a_hex(txt).decode()


def my_aes_decrypt(msg, key, vi):
    """
    AES 算法的解密
    :param msg: 需解密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return: 加密后的字符
    """
    msg = binascii.a2b_hex(msg)
    obj = AES.new(key, AES.MODE_CBC, vi)
    return obj.decrypt(msg).decode()


def my_sha1_seed(msg, seed):
    """
    sha1加盐加密
    :param msg: 加密数据
    :param seed: 盐
    :return:
    """
    seed = seed.encode("utf-8")
    msg = msg.encode("utf-8")
    dk = pbkdf2_hmac('sha1', msg, seed, 100, 64)
    # 转换成十六进制对应的字符串
    return binascii.hexlify(dk).decode()


def my_sha256_seed(msg, seed):
    """
    sha1加盐加密
    :param msg: 加密数据
    :param seed: 盐
    :return:
    """
    seed = seed.encode("utf-8")
    msg = msg.encode("utf-8")
    dk = pbkdf2_hmac('sha256', msg, seed, 100, 64)
    # 转换成十六进制对应的字符串
    return binascii.hexlify(dk).decode()


def get_sha256(data, key):
    # HmacSHA256加密算法
    key = key.encode('utf-8')       # sha256加密的key
    message = data.encode('utf-8')  # 待sha256加密的内容
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    # sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest()).decode()
    return sign
