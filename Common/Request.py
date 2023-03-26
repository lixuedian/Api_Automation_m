# -*- coding: utf-8 -*-
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Request.py
# 开发工具 ： PyCharm

"""
封装request

"""
import os
import random
import requests
import Common.Consts
from requests_toolbelt import MultipartEncoder
from Common import Log
from Config.Config import Config
from Mode.body_data import json_to_get
import json


class Request:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    #     """
    #     :param env:
    #     """
    #     self.session = Session.Session()
    #     self.get_session = self.session.get_session(env)

    def get_request(self, url, data, header, f_type=None):
        """
        Get请求
        :param f_type:
        :param url:
        :param data:
        :param header:
        :return:

        """
        if url.startswith('https://') or url.startswith('http://'):
            # url = '%s%s' % ('http://', self.config.test04_unified_url+url)
            url = url
        else:
            url = '%s%s' % ('http://', url)
            # print('url={}'.format(url))
        # self.log.info("请求头为：{}".format(header))
        # self.log.info("请求方法为：{}".format("get"))
        # self.log.info("请求url为：{}".format(url))
        # self.log.info("请求数据为：{}".format(data))
        try:
            if data is None:
                self.request_log(url=url, method='get', headers=header)
                response = requests.get(url=url, headers=header)
            else:
                if f_type == 'json':
                    data = json.dumps(data)
                    header['Content-Type'] = "application/json"
                    self.request_log(url=url, method='get', data=data, headers=header)
                    response = requests.get(url=url, data=data, headers=header)
                else:
                    self.request_log(url=url, method='get', params=data, headers=header)
                    response = requests.get(url=url, params=data, headers=header)
                # request_headers = response.request.headers
            # print('Get.response  request_headers={} '.format(request_headers))
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()
        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()
        try:
            self.log.info("响应数据为：{}".format(response.json()))
            return response.json()
        except:
            self.log.info("响应数据非json格式数据")

    def post_request(self,  url, data, header, f_type=None):
        """
        Post请求
        :param f_type:
        :param url:
        :param data:
        :param header:
        :return:

        """
        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)
            # print('url={}'.format(url))

        try:
            if data is None:
                self.request_log(url=url, method='post', headers=header)
                response = requests.post(url=url, headers=header)
            else:
                if f_type:
                    if f_type == "data":
                        data = data
                        header['Content-Type'] = "application/x-www-form-urlencoded"
                    elif f_type == "json":
                        data = json.dumps(data)
                        header['Content-Type'] = "application/json"
                self.request_log(url=url, method='post', data=data, headers=header)
                response = requests.post(url=url, headers=header, data=data)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)
        try:
            response_dicts = dict()
            response_dicts = response.json()
            # response_dicts['code'] = response.status_code
            # try:
            #     response_dicts['body'] = response.json()
            # except Exception as e:
            #     print(e)
            #     response_dicts['body'] = ''
            #
            # response_dicts['text'] = response.text
            response_dicts['time_consuming'] = time_consuming
            # response_dicts['time_total'] = time_total
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def post_request_files(self, url, data, header, file_parm, file):
        """
        提交Multipart/form-data 格式的Post请求
        上传文件使用该方法
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :return:
        """
        # if not url.startswith('https://'):
        #     url = '%s%s' % ('https://', self.config.test04_unified_url+url)
        #     print('url={}'.format(url))
        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                # data[file_parm] = os.path.basename(file), open(file, 'rb')
                data[file_parm] = ('unnamed.jpg', open(file, 'rb'), 'image/jpeg')
                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                self.request_log(url=url, method='post', headers=header, files=file)
                response = requests.post(url=url,  headers=header, data=enc)
                # response = requests.post(url=url, headers=h, data=multipart_encoder)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        # response_dicts = dict()
        response_dicts = response.json()
        # response_dicts['code'] = response.status_code
        # try:
        #     response_dicts['body'] = response.json()
        # except Exception as e:
        #     print(e)
        #     response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        try:
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def post_request_urlencoded(self, url, data, header):
        """
        提交x-www-form-urlencoded 格式的Post请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        # if not url.startswith('http://'):
        #     url = '%s%s' % ('http://', self.config.test_user_url+url)
        #     print('url={}'.format(url))
        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)
        try:
            data = json_to_get(data)
            url = url+'?'+data
            self.request_log(url=url, method='post', data=data, headers=header)
            response = requests.post(url=url, headers=header)
            # print(response.json())
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()
        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()
        try:
            response_dicts = response.json()
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                self.request_log(url=url, method='put', data=data, headers=header)
                response = requests.put(url=url, data=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()
        try:
            response_dicts = response.json()
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def delete_request(self, url, data, header, f_type=None):
        """
        delete请求
        :param url:
        :param data:
        :param header:
        :return:

        """

        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)
        try:
            if f_type == 'json':
                data = json.dumps(data)
                header['Content-Type'] = "application/json"
                response = requests.delete(url=url, data=data, headers=header)
                self.request_log(url=url, method='delete', params=data, headers=header)
            elif f_type == 'data':
                response = requests.delete(url=url, params=data, headers=header)
                self.request_log(url=url, method='delete', params=data, headers=header)
            else:
                response = requests.delete(url=url + str(data), headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        # response_dicts['code'] = response.status_code
        try:
            response_dicts = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        # response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        try:
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def patch_request(self, url, data, header):
        """
        patch请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if url.startswith('https://') or url.startswith('http://'):
            url = url
        else:
            url = '%s%s' % ('https://', url)

        try:
            if data is None:
                response = requests.patch(url=url, headers=header)
            else:
                self.request_log(url=url, method='patch', data=data, headers=header)
                response = requests.patch(url=url, data=json.dumps(data), headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()
        try:
            response_dicts = response.json()
            self.log.info("响应数据为：{}".format(response_dicts))
            return response_dicts
        except AssertionError:
            self.log.info("响应数据非json格式数据")

    def request_log(self, url=None, method=None, data=None,  params=None, headers=None, files=None,
                    cookies=None, **kwargs):
        self.log.info("接口请求地址 ==>> {}".format(url))
        if method:
            self.log.info("接口请求方式 ==>> {}".format(method))
            # print("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        if headers:
            self.log.info("接口请求头 ==>> {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
            # print("接口请求头 ==>> {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
        if params:
            self.log.info("接口请求 params 参数 ==>> {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
            # print("接口请求 params 参数 ==>> {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
        if data:
            self.log.info("接口参数 ==>> {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
            # print("接口参数 ==>> {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
        # log.info("接口请求体 json 参数 ==>> {}".format(complexions.dumps(json, indent=4, ensure_ascii=False)))
        if files:
            self.log.info("接口上传附件 files 参数 ==>> {}".format(files))
            # print("接口上传附件 files 参数 ==>> {}".format(files))
        if cookies:
            self.log.info("接口 cookies 参数 ==>> {}".format(json.dumps(cookies, indent=4, ensure_ascii=False)))
            # print("接口 cookies 参数 ==>> {}".format(json.dumps(cookies, indent=4, ensure_ascii=False)))

# if __name__ == '__main__':
#     config =Config()
#     a = config.get_conf('parameter','evse_nos')
#     lsa = json.loads(a)
#     print(a)
#     print(lsa)
#     print(lsa[0])
