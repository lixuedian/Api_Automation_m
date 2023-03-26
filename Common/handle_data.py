
import re
from Common.Log import MyLog
from Config.Config import Config
config = Config()


class EnvData:
    """
    存储用例要使用到的数据。
    """
    pass


def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


def replace_case_by_regular(case):
    """
    对excel当中，读取出来的整条测试用例，做全部替换。
    包括url,request_data,expected,check_sql
    """
    for key, value in case.items():
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_by_regular(value)
    # MyLog().info("正则表达式替换完成之后的请求数据：\n{}".format(case))
    return case


def replace_by_regular(data):
    """
    前置数据替换和配置文件数据 替换
    将字符串当中，匹配#(.*?)#部分，替换换对应的真实数据。
    真实数据只从2个地方去获取：1个是配置文件当中的data区域 。另1个是，EvnData的类属性。
    data: 字符串
    return: 返回的是替换之后的字符串

    ps： 1个是配置文件当中的data区域 。另1个是，EvnData的类属性。必须都是字符串类型。
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表。
    # 标识符对应的值，来自于：1、环境变量  2、配置文件   从原始字符串中 提取标识符 自己要替换的标识符
    if res:
        for item in res:
            # 得到标识符对应的值。
            try:
                # 配置文件中保存的固定的数据
                value = config.get_conf('data', item)
            except:
                try:
                    # 从全局环境变量中提取数据
                    value = getattr(EnvData, item)
                except AttributeError:
                    # 如果没有提取到数据 则结束循环
                    # value = "#{}#".format(item)
                    continue
            # print(value)
            # 再去替换原字符串  替换自定义的变量为自己想要的数据
            data = data.replace("#{}#".format(item), value)
    return data


def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case

