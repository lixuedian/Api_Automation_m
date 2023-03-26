"""
封装requests请求
"""
import requests
from Common import Log
from Config.Config import Config
config = Config()
log = Log.MyLog()


def send_requests(method, url, data=None, token=None):
    """
    :param method:
    :param url:
    :param data:字典形式的数据。
    :param token:
    :return:
    """
    log.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(token)
    # 得到完整的url - 拼接url
    url = __pre_url(url)
    # 请求数据的处理 - 如果是字符串，则转换成字典对象。
    data = __pre_data(data, token)
    # 将请求数据转换成字典对象。
    log.info("请求头为：{}".format(headers))
    log.info("请求方法为：{}".format(method))
    log.info("请求url为：{}".format(url))
    log.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        # resp = requests.post(url, params=data, headers=headers)
        resp = requests.post(url, data=data, headers=headers)
    log.info("响应状态码为：{}".format(resp.status_code))
    try:
        log.info("响应数据为：{}".format(resp.json()))
        return resp.json()
    except:
        log.info("非json格式数据")



def __handle_header(token=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = token
    return headers


def __pre_url(url):
    """
    拼接接口的url地址。
    """
    base_url = config.get_conf('server', 'umc_url')
    # 判断要拼接的字符串是否是/开始
    if url.startswith("/"):
        return base_url + url
    elif url.startswith("http://") or url.startswith("https://"):
        # 如果是完整的url路径就直接返回该url 无需再次处理
        return url
    else:
        return base_url + "/" + url


def __pre_data(data, token=None):
    """
    如果data是字符串，则转换成字典对象。
    """
    if data is not None and isinstance(data, str):
        # 如果有null，则替换为None
        if data.find("null") != -1:
            data = data.replace("null", "None")
        # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
        data = eval(data)

    return data
