# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/14 10:47
# 文件名称 ： __init__.py.py
# 开发工具 ： PyCharm
import os

from Common.Delete import delete_file

dir_path = os.path.abspath(os.path.dirname(__file__))
file_log = dir_path + '/log.log'
file_err = dir_path + '/err.log'


def delete_log():
    # delete_file(file_log)
    # delete_file(file_err)
    with open(file_log, 'r+') as file:
        file.truncate(0)
    with open(file_err, 'r+') as file:
        file.truncate(0)
