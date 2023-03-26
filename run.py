"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块
# '--allure_features=测试features'
"""

import pytest

from Common import Log, GToken
from Common import Shell
from Common.Email import get_report_file
from Config import Config
from Common import Email
from Log import delete_log

conf = Config.Config()
log = Log.MyLog()
shell = Shell.Shell()

if __name__ == '__main__':
    # 清空log日志
    delete_log()
    # token初始化
    GToken.init()
    # 清空allure数据
    conf.delete_file()
    log.info('初始化配置文件, path=' + conf.conf_path)
    report_path = conf.path_dir+'/Report'
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]  # 执行所有测试用例
    # args = ['-s', './test_case/test_admin', '-q', '--alluredir', xml_report_path]  # 按目录去执行测试用例
    pytest.main(args)

    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    pytest_html = 'pytest --html=%s/report.html --self-contained-html' % report_path
    try:
        shell.invoke(cmd)
        shell.invoke(pytest_html)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
    # try:
    #     report_file = get_report_file(report_path)
    #     mail = Email.SendMail()
    #     mail.send_mail(report_file)
    # except Exception as e:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise

