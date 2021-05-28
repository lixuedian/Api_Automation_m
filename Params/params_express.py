import os
from Common import Log
from Params.params import get_parameter
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class GetExpressList:
    params = get_parameter('getExpressList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetExpressTracesOne:
    params = get_parameter('getExpressTracesOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class SetExpressOne:
    params = get_parameter('setExpressOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])

