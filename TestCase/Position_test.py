
import allure
import pytest
from Common.Methodes import notify
from Config.Config import Config
from Params.params_position import *
from Common import Log
from Common import Consts
from Common.Parser import parser

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config = Config()
notify = notify()
log = Log.MyLog()
url = config.test_Position_url


class TestBanner(object):
    data = Banner()
    case_data = data.case_data

    @allure.description('根据type获取不同类型轮播图')
    @pytest.mark.parametrize('case', case_data)
    def test_01_banner(self, case):
        TestBanner.test_01_banner.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestRegion(object):
    data = Region()
    case_data = data.case_data

    @allure.description('获取所有省份')
    @pytest.mark.parametrize('case', case_data)
    def test_02_region(self, case):
        TestRegion.test_02_region.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestRegionCity(object):
    data = RegionCity()
    case_data = data.case_data

    @allure.description('根据provinceId获取下辖所有市信息')
    @pytest.mark.parametrize('case', case_data)
    def test_03_region_city(self, case):
        TestRegionCity.test_03_region_city.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestRegionCityRegion(object):
    data = RegionCityRegion()
    case_data = data.case_data

    @allure.description('根据cityId获取下辖所有区县信息')
    @pytest.mark.parametrize('case', case_data)
    def test_04_region_city_region(self, case):
        TestRegionCityRegion.test_04_region_city_region.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionList(object):
    data = PositionList()
    case_data = data.case_data

    @allure.description('获取职位列表')
    @pytest.mark.parametrize('case', case_data)
    def test_05_position_list(self, case):
        TestPositionList.test_05_position_list.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestCollect(object):
    data = Collect()
    case_data = data.case_data

    @allure.description('添加收藏')
    @pytest.mark.parametrize('case', case_data)
    def test_06_collect(self, case):
        TestCollect.test_06_collect.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestCancel(object):
    data = Cancel()
    case_data = data.case_data

    @allure.description('取消收藏')
    @pytest.mark.parametrize('case', case_data)
    def test_07_cancel(self, case):
        TestCancel.test_07_cancel.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestCollectList(object):
    data = CollectList()
    case_data = data.case_data

    @allure.description('我的职位收藏列表')
    @pytest.mark.parametrize('case', case_data)
    def test_08_collect_list(self, case):
        TestCollectList.test_08_collect_list.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionDetail(object):
    data = PositionDetail()
    case_data = data.case_data

    @allure.description('分页获取职位列表')
    @pytest.mark.parametrize('case', case_data)
    def test_09_position_detail(self, case):
        TestPositionDetail.test_09_position_detail.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionFind(object):
    data = PositionFind()
    case_data = data.case_data

    @allure.description('根据id获取职位详情')
    @pytest.mark.parametrize('case', case_data)
    def test_10_position_find(self, case):
        TestPositionFind.test_10_position_find.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionDataList(object):
    data = PositionDataList()
    case_data = data.case_data

    @allure.description('职位招聘历年数据统计表')
    @pytest.mark.parametrize('case', case_data)
    def test_11_position_find(self, case):
        TestPositionDataList.test_11_position_find.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionYearList(object):
    data = PositionYearList()
    case_data = data.case_data

    @allure.description('无条件获取年份列表')
    @pytest.mark.parametrize('case', case_data)
    def test_12_position_year_list(self, case):
        TestPositionYearList.test_12_position_year_list.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')


class TestPositionQueryList(object):
    data = PositionQueryList()
    case_data = data.case_data

    @allure.description('获取最近职位查询用户信息')
    @pytest.mark.parametrize('case', case_data)
    def test_13_position_query_list(self, case):
        TestPositionQueryList.test_13_position_query_list.__doc__ = case['test_name']
        log.info('test_name={}, url={}, data={}, header={}'.
                 format(case['test_name'], url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        Consts.RESULT_LIST.append('True')
