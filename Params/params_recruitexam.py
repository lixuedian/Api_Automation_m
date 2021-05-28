"""
定义所有测试数据

"""
import os
from Common import Log
from Params.params import get_parameter
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class GetRecruitExamList:
    params = get_parameter('getRecruitExamList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetShiJuanList:
    params = get_parameter('getShijuanList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAdList:
    params = get_parameter('getAdList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTakeExamList:
    params = get_parameter('getTakeExamList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AdGiveProduct:
    params = get_parameter('adGiveProduct')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
