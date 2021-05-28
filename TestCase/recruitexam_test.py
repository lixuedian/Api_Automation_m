
import allure
import pytest
from Common.Methodes import notify
from Config.Config import Config
from Params.params_recruitexam import *
from Common import Log
from Common import Consts
from Common.Parser import parser
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config = Config()
notify = notify()
log = Log.MyLog()
url = config.test_shijian_url
url = '%s%s' % ('http://', url)


class TestGetRecruitExamList(object):
    data = GetRecruitExamList()
    case_data = data.case_data

    @allure.description('获取招考列表')
    @pytest.mark.parametrize('case', case_data)
    def test_recruitexam_01(self, case):
        TestGetRecruitExamList.test_recruitexam_01.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')

    data = GetShiJuanList()
    case_data = data.case_data

    @allure.description('获取估分试卷列表')
    @pytest.mark.parametrize('case', case_data)
    def test_recruitexam_02(self, case):
        TestGetRecruitExamList.test_recruitexam_02.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')

    data = GetAdList()
    case_data = data.case_data

    @allure.description('获取招考广告接口')
    @pytest.mark.parametrize('case', case_data)
    def test_recruitexam_03(self, case):
        TestGetRecruitExamList.test_recruitexam_03.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')

    data = GetTakeExamList()
    case_data = data.case_data

    @allure.description('估分，领资料 首页气泡数据V2版本')
    @pytest.mark.parametrize('case', case_data)
    def test_recruitexam_04(self, case):
        TestGetRecruitExamList.test_recruitexam_04.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')

    data = AdGiveProduct()
    case_data = data.case_data

    @allure.description('赠送课程_New')
    @pytest.mark.parametrize('case', case_data)
    def test_recruitexam_05(self, case):
        TestGetRecruitExamList.test_recruitexam_05.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')
