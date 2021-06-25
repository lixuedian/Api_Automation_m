import os
from Common import Log
from Params.params import get_parameter
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class Logout:
    """登出"""
    params = get_parameter('Logout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Permission:
    """获取用户具体权限"""
    params = get_parameter('permission')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Sso:
    """sso接口，判断用户是否已登陆"""
    params = get_parameter('sso')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RoleLIst:
    """根据部门获取已绑定相关角色"""
    params = get_parameter('role_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
