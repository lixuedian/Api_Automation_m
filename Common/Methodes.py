# _*_ coding : UTF-8
# 开发时间 ： 2020/12/18 8:22
# 文件名称 ： Methodes.py
# 开发工具 ： PyCharm
"""
封装的request请求
"""
import json

from Common import Request
from Config.Config import Config
from Common import Log

request = Request.Request()
config = Config()
log = Log.MyLog()


class Notify:
    @staticmethod
    def token():
        pass

    def notify_result(self, mode, url, data, header, f_type=None, file=None):
        # 请求方式
        numbers = {
            0: self.get_request,
            1: self.post_request,
            2: self.post_request_files,
            3: self.post_request_urlencoded,
            4: self.put_request,
            5: self.delete_request,
            6: self.patch_request
        }
        header = {'Cookie': config.get_conf('parameter', 'cookie')}
        method = numbers.get(mode)
        if mode:
            if f_type:
                res = method(url, data, header, f_type)
            elif file:
                res = method(url, data, header, file)
            else:
                res = method(url, data, header)
            return res
        elif mode == 0:
            if f_type:
                res = method(url, data, header, f_type)
            else:
                res = method(url, data, header)
            return res
        else:
            assert AssertionError
        # if mode == 1:
        #     if f_type:
        #         res = self.post_request(url, data, header, f_type)
        #     else:
        #         res = self.post_request(url, data, header)
        #     return res
        # elif mode == 3:
        #     res = method(url, data, header)
        #     return res
        # elif mode == 2:
        #     res = self.post_request_files(url, data, header, file)
        #     return res
        # elif mode == 4:
        #     if f_type:
        #         res = self.put_request(url, data, header, f_type)
        #         return res
        # elif mode == 6:
        #     res = self.patch_request(url, data, header)
        #     return res
        # elif mode == 0:
        #     if f_type:
        #         res = self.get_request(url, data, header, f_type)
        #     else:
        #         res = self.get_request(url, data, header)
        #     return res
        # elif mode == 5:
        #     if f_type:
        #         res = method(url, data, header, f_type)
        #     else:
        #         res = method(url, data, header)
        #     return res
        # else:
        #     assert AssertionError

    @staticmethod
    def get_request(url, data, header, f_type=None):
        """
        获取枪头详情信息
        :param f_type:
        :param url:
        :param data:
        :param header:
        :return:
        """
        if f_type:
            result = request.get_request(url, data, header, f_type)
            return result
        else:
            result = request.get_request(url, data, header)
            return result

    @staticmethod
    def post_request(url, data, header, f_type=None):
        """
        根据用户，枪头编号查询可用账户
        :param f_type:
        :param url:
        :param data:
        :param header:
        :return:
        """
        if f_type:
            result = request.post_request(url, data, header, f_type)
        else:
            result = request.post_request(url, data, header)
        return result

    def post_request_files(self, url, data, header, file):
        """
        获取幂等型接口调用所需的token
        :param file: 文件路径
        :param url:
        :param data:
        :param header:
        :return:
        """
        result = request.post_request_files(url, data, header, 'file', file)
        return result

    def post_request_urlencoded(self, url, data, header):
        # header['token'] = self.token()
        header['Authorization'] = self.token()
        result = request.post_request_urlencoded(url, data, header)
        return result

    def put_request(self, url, data, header, f_type=None):
        try:
            if header['Authorization']:
                pass
        except KeyError:
            header['Authorization'] = self.token()
        # header['token'] = self.token()
        # header['Authorization'] = self.token()
        if f_type:
            if f_type == "data":
                data = data
                header['Content-Type'] = "application/x-www-form-urlencoded"
            elif f_type == "json":
                data = json.dumps(data)
                header['Content-Type'] = "application/json"
        result = request.put_request(url, data, header)
        return result

    def delete_request(self, url, data, header, f_type=None):
        try:
            if header['Authorization']:
                pass
        except KeyError:
            header['Authorization'] = self.token()
        if f_type:
            result = request.delete_request(url, data, header, f_type)
        else:
            result = request.delete_request(url, data, header)
        return result

    def patch_request(self, url, data, header):
        # header['token'] = self.token()
        try:
            if header['Authorization']:
                pass
        except KeyError:
            header['Authorization'] = self.token()
        header['Content-Type'] = "application/json"
        result = request.patch_request(url, data, header)
        return result
