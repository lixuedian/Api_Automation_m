# -*- coding: utf-8 -*-
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Assert.py
# 开发工具 ： PyCharm

"""
封装Assert方法

"""
from Common import Log
from Common import Consts
import json

from Common.Mysql_operate import MysqlDb
from Config.Config import Config

# db = MysqlDb(Config().mysql_conf('mysql'))


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except AssertionError:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except AssertionError:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            self.log.info("PASS ==>> 预期结果：{}， 实际结果：{}".format(body, expected_msg))
            return True

        except AssertionError:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg, test_name):
        """
        验证response body中是否等于预期字符串
        :param test_name:
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            self.log.info("PASS ==>> 预期结果：{}， 实际结果：{}".format(body, expected_msg))
            return True

        except AssertionError:
            self.log.error("%s,Fail ==>> 预期结果: %s, 实际结果: %s" % (test_name, expected_msg, body))
            self.log.info("*************** 结束执行用例 ***************")
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except AssertionError:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')
            raise

    # def assert_sql(self, s_sql):
    #     """
    #     查询数据是否存在
    #     :param s_sql:
    #     :return:
    #     """
    #     count = db.get_count(s_sql)
    #     try:
    #         assert count == 1
    #         self.log.info('PASS ==>>执行{}得到的数据{}'.format(s_sql, count))
    #     except AssertionError:
    #         self.log.error("Fail ==>> 预期结果: %s, 实际结果: %s" % (s_sql, count))
    #         self.log.info("断言失败！")
    #         raise
    #
    # def assert_msql(self, sql, msg):
    #     """
    #     对数据进行比对
    #     :param msg:
    #     :param sql:
    #     :return:
    #     """
    #     count = db.select_db(sql)
    #     try:
    #         msq = ''
    #         for item in count:
    #             for key in item:
    #                 msq = item[key]
    #         assert msq == msg
    #         self.log.info('PASS ==>>执行{},预期结果: {}, 实际结果: {}'.format(sql, msg, count))
    #     except AssertionError:
    #         self.log.error("Fail ==>>执行%s, 预期结果: %s, 实际结果: %s" % (sql, msg, count))
    #         self.log.info("断言失败！")
    #         raise
