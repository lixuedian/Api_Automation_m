# -*- coding: utf-8 -*-
"""
    项目名称： test_main
    文件名： GoogleCode.py 
    创建人： xuejian
    使用软件: PyCharm
    创建时的系统日期： 2022/7/5
    创建时的系统时间：14:38
    年-月-日  2022-07-05
    时:分:秒	 14:38:56	
    英文月份缩写 7月
    英文月份全称 七月
"""
import hmac, base64, struct, hashlib, time

from Config.Config import Config
from Common.Mysql_operate import MysqlDb


class CalGoogleCode():
    """计算谷歌验证码（16位谷歌秘钥，生成6位验证码）"""

    # 使用静态方法，调用这个方法时，不必对类进行实例化
    @staticmethod
    def cal_google_code(secret='7S66EGU4KMV4MJKUB6RMVUQ4S4FKFLFN', current_time=int(time.time()) // 30):
        """
        :param secret:   16位谷歌秘钥
        :param current_time:   时间（谷歌验证码是30s更新一次）
        :return:  返回6位谷歌验证码
        """
        key = base64.b32decode(secret)
        msg = struct.pack(">Q", current_time)
        google_code = hmac.new(key, msg, hashlib.sha1).digest()
        o = ord(chr(google_code[19])) & 15  # python3时，ord的参数必须为chr类型
        google_code = (struct.unpack(">I", google_code[o:o + 4])[0] & 0x7fffffff) % 1000000
        return '%06d' % google_code  # 不足6位时，在前面补0

    @staticmethod
    def google_code(mobile):
        sql = "select google_secret from user_base_info  where mobile ={}".format(mobile)
        db = MysqlDb(Config().mysql_conf('mysql'))
        secret = db.select_db(sql)
        for item in secret:
            for key in item:
                secret = item[key]
        return CalGoogleCode.cal_google_code(secret)


# if __name__ == '__main__':
#     secret_key = "7S66EGU4KMV4MJKUB6RMVUQ4S4FKFLFN"
#     print(CalGoogleCode.cal_google_code())    # 并未实例化CalGoogleCode，也可以调用它的方法

