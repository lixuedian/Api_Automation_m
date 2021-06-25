import allure
import pytest
from Common import Consts
from Params.params_ht import *
from Common.Parser import parser
from Common.Methodes import Notify
import TestCase.交易中台.权限

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
url = TestCase.交易中台.权限.url
header = TestCase.交易中台.权限.header


class TestAuthority(object):

    @allure.description('根据部门获取已绑定相关角色')
    @pytest.mark.parametrize('case', RoleLIst().case_data)
    def test_authority_01(self, case):
        TestAuthority.test_authority_01.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = Notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
