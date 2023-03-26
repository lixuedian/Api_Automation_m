import sys 
import jsonpath
from Common.handle_data import EnvData
from Common.handle_redis import redis_helper
from Common.params import log
sys.path.append("./")


def check_redis_from_response(extract_exprs):
    "从redis中获取数据后 并根据key动态添加EnvData数据中"
    # 将提取表达式转换成字典
    extract_dict = eval(extract_exprs)
    log.info("从redis中获取的key值: \n {}".format(extract_dict))
    for key, value in extract_dict.items():
        log.info("通过该key从redis中获取值：{}".format(value))
        res = redis_helper.get_value_hash(value)
        # 获取值有两种方式 一种是从hash值获取，一种是获取字符串
        if len(res) == 0:
            res = redis_helper.get_value_str(value)
        log.info("设置环境变量.key:{},value:{}".format(key, res))
        setattr(EnvData, key, res)


def extract_data_from_response(extract_exprs, response_dict):
    """
    根据jsonpath提取表达式，从响应结果当中，提取数据并设置为环境变量EnvData类的类属性，作为全局变量使用。
    :param extract_exprs: 从excel当中读取出来的，提取表达式的字符串。
    :param response_dict: http请求之后的响应结果。
    :return:Nonoe
    """
    # 将提取表达式转换成字典
    extract_dict = eval(extract_exprs)
    log.info("要从响应结果当中提取的数据集为：\n{}".format(extract_dict))
    # 遍历字典，key作为全局变量名，value是jsonpath提取表达式。
    for key, value in extract_dict.items():
        # 提取
        res = str(jsonpath.jsonpath(response_dict, value)[0])
        # 设置环境变量
        log.info("设置环境变量.key:{},value:{}".format(key, res))
        setattr(EnvData, key, res)


def db_code(key, num, mobile):
    """
    查询短信验证码
    num=0, 注册验证码
    num=1, 登录验证码
    num=2, 提现验证码
    num=3， 修改登录密码
    num=4， 修改交易密码
    num=5， 用户账号提醒：【Bitvito】您的USDT合约账户风险度已超过90%（达到100%将进入爆仓流程）,请注意及时调整交易策略以避免发生强制平仓。"
    num=11， 【Bitvito】您的$coin$币本位合约，$quantity$仓位已接近强平价格，请注意及时调整交易策略以避免发生强制平仓。
    num=6，【Bitvito】因行情剧烈波动，您的USDT合约账户因资金不足，风险度已达到100%，已被执行强平委托。
    num=12， 【Bitvito】因行情剧烈波动，您的$coin$币本位合约$quantity$，已被执行强平委托。
    num=7，邮箱验证码
    num=13，邮箱登录验证码
    num=8，绑定邮箱
    num=9 绑定手机验证码
    num=10 您正在进行安全验证,您的验证码为
    num=25 谷歌验证码
    num=26 提币邮箱验证码
    num=27 邮箱修改资金密码
    num=14 邮箱修改登录密码
    num=35 admin打款验证码 手机号13810000000
    num=37 邮箱设置API验证码
    num=38 手机设置API验证码
    """

    # num=35，admin打款验证码
    if num == 35:
        ss = "{'" + key + "': 'ADMIN_CACHE:SMS:" + str(num) + "_" + str(mobile) + "'}"
    else:
        ss = "{'" + key + "': 'SMS_" + str(num) + "_" + str(mobile) + "'}"
    check_redis_from_response(ss)


# 手机验证码
db_code('mobile_code', 1, '1234561')
# 邮箱验证码
db_code('email_code', 7, 'qweqwe@163.com')
# admin打款验证码
db_code('admin', 35, '13810000000')
print(EnvData.__dict__)
