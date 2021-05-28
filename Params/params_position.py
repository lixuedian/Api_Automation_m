"""
定义所有测试数据

"""
import os
from Common import Log
from Params.params import get_parameter
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def badydata(locator, key, string):
    # 获取data中要传参数的valve
    olddata = locator['data'][key]
    # 将value和参数拼接新的value
    newdata = olddata % string
    # 将新的value复制给data中对应的key
    locator['data'][key] = newdata
    # 讲新的locator返回
    return locator


class Banner:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('banner')
    case_data = []
    for i in range(0, len(params)):
        # badydata(params, i, 3)
        case_data.append(params[i])


class Region:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RegionCity:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region_city')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RegionCityRegion:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region_city_region')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Collect:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('collect')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Cancel:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('cancel')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CollectList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('CollectList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionDetail:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_detail')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionFind:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_find')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionDataList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_dataList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionYearList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_yearList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionQueryList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_query_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
