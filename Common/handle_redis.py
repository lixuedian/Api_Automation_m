"""
配置连接redis
1.通过key获取验证码  （短信验证码，邮箱验证码）
2.如果需要清空缓存 通过key进行缓存的清除
"""
from rediscluster import RedisCluster

"""
获取验证码的key拼接
SMS_type_mobile
举例说明
手机号注册验证码 SMS_0_10119070001
手机号修改密码（忘记密码） SMS_3_17319070664   SMS_3_17710830405@163.com
移动端图片码 

"""


class HandleRedis:
    def __init__(self, conn_list):
        self.conn_list = conn_list
        self.connect()

    def connect(self):
        """
        连接redis集群
        :return: object
        """
        try:
            # 非密码连接redis集群
            redisconn = RedisCluster(startup_nodes=self.conn_list, decode_responses=False)
            # # 使用密码连接redis集群
            # redisconn = StrictRedisCluster(startup_nodes=self.conn_list, password='123456')
            self.redisconn = redisconn
        except Exception as e:
            print(e)
            print("错误,连接redis 集群失败")
            return False

    def get_value_str(self, key: str):
        """
        通过key 获取value值
        """
        try:
            return self.redisconn.get(key).decode()
        except:
            return ""

    def get_value_hash(self, key: str):
        """
        通过key 获取value值
        """
        try:
            return self.redisconn.hget(key, "code").decode()
        except:
            return ""

    def get_render_str(self, key):
        """
        通过手机号或者邮箱账号获取图形验证码
        图形验证码的key组合
        """
        render_key = "KAPTCHA_SESSION_KEY_{}".format(key)
        return self.get_value_hash(render_key)

    def delete_value_str(self, key: str):
        """
        删除key
        """
        try:
            return self.redisconn.delete(key).decode()
        except:
            return ""


redis_basis_conn = [{'host': '172.30.96.24', 'port': 7000},
                    {'host': '172.30.96.24', 'port': 7001},
                    {'host': '172.30.96.24', 'port': 7002},
                    {'host': '172.30.96.24', 'port': 7003},
                    {'host': '172.30.96.24', 'port': 7004},
                    {'host': '172.30.96.24', 'port': 7005}, ]
redis_helper = HandleRedis(redis_basis_conn)

if __name__ == '__main__':
    redis_basis_conn = [{'host': '172.30.96.24', 'port': 7000},
                        {'host': '172.30.96.24', 'port': 7001},
                        {'host': '172.30.96.24', 'port': 7002},
                        {'host': '172.30.96.24', 'port': 7003},
                        {'host': '172.30.96.24', 'port': 7004},
                        {'host': '172.30.96.24', 'port': 7005}, ] 
    redis_helper = HandleRedis(redis_basis_conn)
    # OPEN_API_TOKEN:767e44015a264307ace435d6973694de  open_api token key
    # verify_code_error_time_uid # 登录验证码错误次数
    # SETTLE_CACHE:TAP:20220915 每天奖励给用户盈利加成的金额上限

    # print(redis_helper.get_value_str('verify_code_error_time_1066448900718597'))
    print(redis_helper.get_value_str('SETTLE_CACHE:TAP:20220915'))
    # redis_helper.delete_value_str('OPEN_API_TOKEN:c512d75225b240a5a803def08886a321')
    # redis_helper.delete_value_str('open-api:rate_limit:1066448900718597')  # open-api用户限制访问次数
    # redis_helper.delete_value_str('verify_code_error_time_1066448900718597')  # 登录验证码错误次数
    # redis_helper.delete_value_str('SETTLE_CACHE:TAP:20220915')  # 登录验证码错误次数

