import allure
import pytest

import TestCase
from Common import Log
from Common.Assert import Assertions
from Common.Parser import parser
from Common.handle_data import replace_case_by_regular
from Common.params import load_data
from api.login import Login


@allure.feature('登录')
class TestLOGIN(object):
    def setup(self):
        self.login = Login()
        self.log = Log.MyLog()
        self.Assert = Assertions()

    @allure.description('login')
    @pytest.mark.parametrize('case', load_data("login", "/TestCase/test_login.yaml"))
    def test_login(self, case):
        self.log.info("*************** 开始执行用例 ***************")
        case = replace_case_by_regular(case)
        self.log.info("用例名称  ==>> {}".format(case['test_name']))
        result = self.login.login()
        # parser(result, case['test_name'], case['parser'], case['expected'])
        # 如果check_sql有值，说明要做数据库校验。
        # if case["check_sql"]:
        #     self.Assert.assert_sql(case["check_sql"])
        allure.attach.file(TestCase.BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名',
                           allure.attachment_type.TEXT)
