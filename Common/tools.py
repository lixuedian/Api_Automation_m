# -*- coding: utf-8 -*-
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： tools.py
# 开发工具 ： PyCharm
"""
读取yaml测试数据

"""

import yaml
import os
import os.path


def parse(yaml_PATH):
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_ya = BASE_PATH + yaml_PATH
    pages = {}

    with open(path_ya, 'rb') as f:
        page = yaml.safe_load(f)
        pages.update(page)
    return pages


class GetPages:
    @staticmethod
    def get_page_list(yaml_PATH):
        _page_list = {}
        pages = parse(yaml_PATH)
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []
            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list
        return _page_list


def badydata(locator, key, string):
    # 获取data中要传参数的valve
    olddata = locator['data'][key]
    # 将value和参数拼接新的value
    newdata = olddata % string
    # 将新的value复制给data中对应的key
    locator['data'][key] = newdata
    # 讲新的locator返回
    return locator


def read_testcase_yaml(yaml_name):
    with open(os.getcwd()+"/Params/Param/" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 清除yaml文件
def write_extract_yaml(data):
    with open(os.getcwd()+"/extract.yml", mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清除yaml文件
def clear_extract_yaml():
    with open(os.getcwd()+"/extract.yml", mode='w', encoding='utf-8') as f:
        f.truncate()


class YamlUtil(object):
    pass


def load_data(yaml_name):
    with open(os.getcwd()+"/test_case/" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    list = []
    lists = GetPages.get_page_list()
