import os

import pytest
from Config import Config
from py.xml import html
from selenium import webdriver
from Common import Log

log = Log.MyLog()


def pytest_html_report_title(report):
    """报告标题"""
    report.title = "bitvito_dev环境"


def pytest_configure(config):
    config._metadata.clear()
    # 添加接口地址与项目名称
    config._metadata['接口地址'] = ""
    config._metadata['项目名称'] = "测试环境"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试组")])
    prefix.extend([html.p("测试人员: 李雪殿")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """表头信息"""
    cells.insert(1, html.th('描述'))
    cells.pop(-1)  # 删除link列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop(-1)  # 删除link列


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # 如果你生成的是web ui自动化测试，请把下面的代码注释打开，否则无法生成错误截图
    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):  # 失败截图
    #         file_name = report.nodeid.replace("::", "_") + ".png"
    #         screen_img = capture_screenshot()
    #         if file_name:
    #             html = '<div><img src="data:image/png;base64,%s" alt="screenshot"
    #             style="width:600px;height:300px;" ' \
    #                    'onclick="window.open(this.src)" align="right"/></div>' % screen_img
    #             extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid  # 解决乱码
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


def capture_screenshot():
    """截图保存为base64"""
    driver = webdriver.Chrome()
    return driver.get_screenshot_as_base64()


def pytest_collection_modifyitems(session, items):
    # print(type(items))
    # print("收集到的测试用例:%s" % items)
    # sort排序，根据用例名称item.name 排序
    items.sort(key=lambda x: x.name)
    for item in items:
        print("用例名:%s" % item.name.encode("utf-8").decode("unicode_escape"))


def pytest_sessionfinish(session):
    """测试完成自动生成并打开allure报告"""
    if session.config.getoption('allure_report_dir'):

        try:
            # 判断allure在环境路径中，通常意味着可以直接执行
            if [i for i in os.getenv('path').split(';') if os.path.exists(i) and 'allure' in os.listdir(i)]:
                # 默认生成报告路径为: ./allure-report
                os.system(f"allure generate -c {session.config.getoption('allure_report_dir')}")
                os.system(f"allure open allure-report")
            else:
                log.error('allure不在环境变量中，无法直接生成html报告！')
        except Exception as e:
            log.error(e)


# conftest中设置fixture，目的是当所有用例执行完成后生成allure报告，并清理result下面的json文件
@pytest.fixture(scope="class")
def allure_report(request):
    def clear_result():
        print("所有用例执行完毕")
        result_path = Config.Config().html_report_path
        report_path = Config.Config().xml_report_path
        os.system("allure generate {} -o {} --clean".format(result_path, report_path))
        print("allure报告已生成")
        # 当allure报告生成后，将result中的json文件清空
        for i in os.listdir(result_path):
            file_data = result_path + "\\" + i
            if os.path.isfile(file_data):
                os.remove(file_data)
        print("result下的json文件已清空")
    request.addfinalizer(clear_result)
