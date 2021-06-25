import os
from Common.Parser import parser

import allure
import pytest
from Common.Methodes import Notify
from Config.Config import Config
from Params.params import ShiJuan
from Common import Log
from Common import Consts
from Common import Assert

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestShiJuan(object):
    config = Config()
    noti = Notify()
    log = Log.MyLog()
    data = ShiJuan()
    case_data = data.case_data
    test = Assert.Assertions()

    @allure.feature('这里是一级标签')
    # BLOCKER = 'blocker'　　中断缺陷（客服端程序无响应，无法执行下一步骤）
    # CRITICAL = 'critical'　　临界缺陷（功能点缺失）
    # NORMAL = 'normal'　　普通缺陷（数据计算错误）
    # MINOR = 'minor'　　次要缺陷（界面错误与ui需求不符）
    # TRIVIAL = 'trivial'　　轻微缺陷（必须项无提示，或者提示不规范）
    # @allure.severity('blocker')
    @allure.story('这里是第一个二级标签')
    @allure.description('这是一个测试case')
    @allure.issue(config.test_shijian_url, name='点击我跳转')
    @allure.testcase(config.test_shijian_url)
    @pytest.mark.parametrize('case', case_data)
    def test_shi(self, case):
        TestShiJuan.test_shi.__doc__ = case['test_name']
        config = Config()
        url = config.test_shijian_url
        self.log.info('demo, utl={}, data={}, header={}'.format(url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = self.noti.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        self.log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file((BASE_PATH+'/Log/log.log'), '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
