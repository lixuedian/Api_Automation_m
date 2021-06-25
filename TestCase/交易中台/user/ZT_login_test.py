import allure
import pytest
from Config.Config import Config
from Common import Request
from Common import Consts
from Common import Assert
from Params.params import ZTLogin
from Params.params_ht import *
from Common.Parser import parser
from Common.Methodes import Notify
import requests

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
request = Request.Request()
test = Assert.Assertions()
config = Config()
url = config.test_shijian_url
url = '%s%s' % ('http://', url)


class TestLogin(object):
    header = {
        'token': 'token'
    }

    @allure.description('用户登录')
    @pytest.mark.parametrize('case', ZTLogin().case_data)
    def test_login_zt(self, case):
        log.info('demo, utl={}, data={}, header={}'.format(case['url'], case['data'], case['header']))
        if case['method'] == 'post_request_urlencoded':
            # result = request.post_request_urlencoded(case['url'], case['data'], case['header'])
            result = requests.post(case['url'], params=case['params'], data=case['data'], header=case['header'])
            assert test.assert_text(result['code'], 1, case['test_name'])
            config.write_configuration('Trading', result['data']['token'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('用户登出')
    @pytest.mark.parametrize('case', Logout().case_data)
    def test_logout_zt(self, case):
        TestLogin.test_logout_zt.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = Notify().notify_result(case['mode'], url + case['url'], case['data'], TestLogin.header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')

    @allure.description('获取用户具体权限')
    @pytest.mark.parametrize('case', Permission().case_data)
    def test_logout_zt(self, case):
        TestLogin.test_logout_zt.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = Notify().notify_result(case['mode'], url + case['url'], case['data'], TestLogin.header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')

    @allure.description('sso接口，判断用户是否已登陆')
    @pytest.mark.parametrize('case', Sso().case_data)
    def test_logout_zt(self, case):
        TestLogin.test_logout_zt.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = Notify().notify_result(case['mode'], url + case['url'], case['data'], TestLogin.header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')