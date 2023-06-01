"""
    * 加密
    * @param value 加密数据
    * @param seed 盐
    * @param ts 客户端调用时间戳

# 参数
hash_name:签名算法名；
password:需要加密的二进制编码
salt:加盐
iterations:迭代次数
"""

import json
from Common.Hash import my_sha1_seed, my_sha256


def signature_otc(value, signTime, signUrl, api):
    """
    otc签名
    :param value:
    :param signTime:
    :param signUrl:
    :param api:
    :return:
    """
    value = map_xu(value)
    return my_sha256(value_list(value, signTime, signUrl, api))


def signature(timestamp=None, value=None):
    """
    获取签名信息
    :param timestamp:
    :param value:
    :return:
    """
    seed = "123"
    if value:
        if len(value) >= 0:
            value = map_xu(value)
            value = value_list(value)
        if timestamp:
            seed = str(seed + timestamp)
            return my_sha1_seed(value, seed)
        else:
            return my_sha1_seed(value, seed)
    else:
        if timestamp:
            seed = str(seed + timestamp)
            return my_sha1_seed('', seed)
        else:
            return my_sha1_seed('', seed)


# def make_map(value):
#     """
#     map排序
#     :param value:
#     :return:
#     """
#     after = dict(sorted(value.items(), key=lambda e: e[0]))
#     return after

def map_xu(dict_1):
    """
    排序
    :param dict_1:
    :return:
    """
    item = {}
    if isinstance(dict_1, dict):
        keys = dict_1.keys()
        keys_sort = sorted(keys)
        for key in keys_sort:
            item[key] = map_xu(dict_1[key])
        return item
    elif isinstance(dict_1, list):
        list1 = []
        for b in dict_1:
            b = map_xu(b)
            list1.append(b)
        return list1
    else:
        return dict_1


# def value_list(value):
#     """
#     数据转换
#     :param value:
#     :return:
#     """
#     text = json.loads(json.dumps(value))
#     line = ''
#     for x in text.keys():
#         if len(str(text[x])) == 0:
#             pass
#         else:
#             line_ = f'{x}={text[x]}&'
#             line += line_
#     line = line[:-1]
#     return line


def value_list(value, signTime=None, signUrl=None, api=None):
    """
    数据转换
    :param api:
    :param signUrl:
    :param signTime:
    :param value:
    :return:
    """
    text = json.loads(json.dumps(value))
    line = ''
    for x in text.keys():
        if len(str(text[x])) == 0:
            pass
            # line += x
            # line += '=&'
        else:
            if isinstance(text[x], list):
                line += f'{x}=['
                for y in list(text[x]):
                    if isinstance(y, dict):
                        line += "{"
                    try:
                        for s in y.keys():
                            line_ = f'{s}={y[s]},'
                            line += line_
                        line = line[:-1]
                        if isinstance(y, dict):
                            line += "},"
                    except:
                        line += str(y) + ','
                        # line += ']'
                line = line[:-1]
                line += ']'
            else:
                if text[x] is None:
                    pass
                else:
                    try:
                        if line[-1] == ']':
                            line += '&'
                    except:
                        pass
                    line_ = f'{x}={text[x]}&'
                    line += line_
    if line[-1] == '&':
        line = line[:-1]
    if signTime:
        line += '&secretKey=2ddl5uqicv4xy3avbcqcnu2tdyc3xato&signTime=' + str(
            signTime) + "&signUrl=" + signUrl + ' ' + api
    # if signTime == 0:  # 单独处理
    #     line = ((line.replace('[', '')).replace(']', '')).replace(',', '&orderIdList=')
    # print(line)
    return line


b = {'x-imos-auth_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsaXhkNSIsImlzcyI6ImxpeGQ1IiwiZXhwIjoxNjc5OTIwODMyLCJpYXQiOjE2Nzk4ODQ4MzJ9.Ed1-6CTn2KZaE22-zjMEAsYsrNTlrD8vLnmEAI4_nJQ'}
print(value_list(b))