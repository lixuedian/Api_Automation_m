from Config.Config import Config
from Params.params_shijuan import ReceiveApi
from Common import Consts
from Params.params import ShiJuan
import allure
import pytest
config = Config()
token = config.h_token
urs = config.test_shijian_url
url = '%s%s' % ('http://', urs)
receive = ReceiveApi(url, token)
test = 2
name = '2--有城市001'
# positionType = 2


class TestShiJuan(object):
    data = ShiJuan()
    case_data = data.case_data

    @allure.description('各个字典配置接口 (招考类型，范围, 周期 阶段)')
    @pytest.mark.parametrize('case', case_data)
    def test_sj_01(self, case):
        TestShiJuan.test_sj_01.__doc__ = case['test_name']

        receive.get_recruit_exam_config_data()
        Consts.RESULT_LIST.append('True')

    @allure.description('后台招考列表')
    @pytest.mark.parametrize('case', case_data)
    def test_sj_02(self, case):
        TestShiJuan.test_sj_02.__doc__ = case['test_name']

        """添加招考单条信息"""
        receive.add_recruit_exam_one('2021北京教师招聘考试', test)

        """后台获取招考列表"""
        receive.get_recruit_exam_list()

        """获取招考单条信息"""
        receive.get_recruit_exam_one()

        """修改招考单条信息"""
        receive.set_recruit_exam_one(name, test)

        """线上运营添加接口"""
        receive.add_operation_recruit_exam_one()

        """获取线上运营列表"""
        recruitExamOperationId = receive.get_operation_recruit_exam_list()

        """线上运营启用，禁用，删除接口"""
        receive.set_operation_recruit_exam_one(2)
        receive.set_operation_recruit_exam_one(1)
        receive.set_operation_recruit_exam_one(3)

        """添加绑定素材"""
        receive.add_material_one()
        """获取素材列表"""
        receive.get_material_list()
        """编辑绑定素材"""
        receive.set_material_one()
        receive.get_material_list()
        """删除绑定素材"""
        receive.opt_material_one()

        """删除招考单条信息"""
        receive.opt_recruit_exam_one()

        """获取公众号列表"""
        receive.get_wechat_account_list()

        """生成小程序带参数二维码"""
        receive.create_qrcode()

        """后台获取推广码列表"""
        receive.get_qrcode_list()
        Consts.RESULT_LIST.append('True')

    @allure.description('运营位')
    @pytest.mark.parametrize('case', case_data)
    def test_sj_03(self, case):
        TestShiJuan.test_sj_03.__doc__ = case['test_name']
        """运营位添加接口"""
        receive.add_operate_position_one()
        """运营位修改接口"""
        receive.set_operate_position_one()
        """运营位查询接口"""
        receive.get_operate_position_one()
        """运营位列表接口"""
        receive.get_operate_position_list(2)
        """运营位删除接口"""
        receive.set_operation_position_0ne(2)

    @allure.description('预置位')
    @pytest.mark.parametrize('case', case_data)
    def test_sj_04(self, case):
        """预置位添加接口"""
        receive.add_preset_position_one()
        """获取预置位单条接口"""
        receive.get_preset_position_one()
        """预置位编辑接口"""
        receive.set_preset_position_one()
        """运营位删除接口"""
        receive.set_operation_position_0ne(1)
        Consts.RESULT_LIST.append('True')
