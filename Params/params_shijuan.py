import requests
import json
from Common import Log, Assert

log = Log.MyLog()
test = Assert.Assertions()


class ReceiveApi(object):
    recruitExamId = '',
    recruitExamOperationId = '',
    recruitExamMaterialId = ''
    positionId = ''

    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.h = {
            "token": self.token
        }

    def get_recruit_exam_config_data(self):
        """各个字典配置接口 (招考类型，范围, 周期 阶段)"""
        api = '/admin-recruitexam/getRecruitExamConfigData'
        body = {
            "businessId": 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('各个字典配置接口 (招考类型，范围, 周期 阶段)', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '各个字典配置接口 (招考类型，范围, 周期 阶段)')
        test.assert_text(res['msg'], '成功', '各个字典配置接口 (招考类型，范围, 周期 阶段)')

    def get_recruit_exam_list(self):
        """后台获取招考列表"""
        api = '/admin-recruitexam/getRecruitExamList'
        body = {
            "businessId": 1,
            'page': 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('后台获取招考列表', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '后台获取招考列表)')
        test.assert_text(res['msg'], '成功', '后台获取招考列表)')
        lists = res['data']['lists']
        for list in lists:
            ReceiveApi.recruitExamId = list['recruitExamId']


    def add_recruit_exam_one(self, name, num):
        """添加招考单条信息"""
        api = '/admin-recruitexam/addRecruitExamOne'
        body = {
            "recruitExamName": name,
            "type": num,
            "scale": 1,
            "period": 1,
            "examProvince": "",
            "examCity": "",
            "examCounty": "",
            "stageList": [{
                "recruitStageKey": 1,
                "recruitStageName": "公告",
                "startTime": "2021-04-22",
                "num": 2000,
                "examContent": ""
            },
                {
                    "recruitStageKey": 2,
                    "recruitStageName": "笔试考试",
                    "startTime": "2021-04-23",
                    "num": 2000,
                    "examContent": "1,3"
                },
                {
                    "recruitStageKey": 3,
                    "recruitStageName": "面试考试",
                    "startTime": "2021-04-24",
                    "num": 3000,
                    "examContent": "1,2,3"
                }
            ]
        }
        log.info('test_name={}, url={}, data={}'.
                 format('添加招考单条信息', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=json.dumps(body))
        res = res.json()
        test.assert_text(res['code'], 1, '添加招考单条信息)')
        test.assert_text(res['msg'], '成功', '添加招考单条信息)')

    def get_recruit_exam_one(self):
        """获取招考单条信息"""
        api = '/admin-recruitexam/getRecruitExamOne'
        body = {
            "businessId": 1,
            'recruitExamId': ReceiveApi.recruitExamId
        }
        log.info('test_name={}, url={}, data={}'.
                 format('获取招考单条信息', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '获取招考单条信息)')
        test.assert_text(res['msg'], '成功', '获取招考单条信息)')

    def set_recruit_exam_one(self, name, num):
        """修改招考单条信息"""
        api = '/admin-recruitexam/setRecruitExamOne'
        body = {
            "recruitExamName": name,
            'recruitExamId': ReceiveApi.recruitExamId,
            "type": num,
            "scale": 1,
            "period": 1,
            "examProvince": "河北省",
            "examCity": "邢台市",
            "examCounty": "清河县",
            "stageList": [{
                "recruitStageKey": 1,
                "recruitStageName": "公告",
                "startTime": "2021-04-22",
                "num": 2000,
                "examContent": ""
            },
                {
                    "recruitStageKey": 2,
                    "recruitStageName": "笔试考试",
                    "startTime": "2021-04-23",
                    "num": 2000,
                    "examContent": "1,3"
                },
                {
                    "recruitStageKey": 3,
                    "recruitStageName": "面试考试",
                    "startTime": "2021-04-24",
                    "num": 3000,
                    "examContent": "1,2,3"
                }
            ]
        }
        log.info('test_name={}, url={}, data={}'.
                 format('修改招考单条信息', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=json.dumps(body))
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '修改招考单条信息)')
        test.assert_text(res['msg'], '成功', '修改招考单条信息)')

    def opt_recruit_exam_one(self):
        """删除招考单条信息"""
        api = '/admin-recruitexam/optRecruitExamOne'
        body = {
            "businessId": 1,
            "recruitExamId": ReceiveApi.recruitExamId
        }
        log.info('test_name={}, url={}, data={}'.
                 format('删除招考单条信息', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '删除招考单条信息)')
        test.assert_text(res['msg'], '成功', '删除招考单条信息)')

    def get_operation_recruit_exam_list(self):
        """获取线上运营列表"""
        api = '/admin-recruitexam/getOperationRecruitExamList'
        body = {
            "recruitExamId": ReceiveApi.recruitExamId,
            "page": 1,
            "pageSize": 10
        }
        log.info('test_name={}, url={}, data={}'.
                 format('获取线上运营列表', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '获取线上运营列表)')
        test.assert_text(res['msg'], '成功', '获取线上运营列表)')
        lists = res['data']['lists']
        for list in lists:
            ReceiveApi.recruitExamOperationId = list['recruitExamOperationId']

    def set_operation_recruit_exam_one(self, optType):
        """线上运营启用，禁用，删除接口"""
        api = '/admin-recruitexam/setOperationRecruitExamOne'
        body = {
            "recruitExamOperationId": ReceiveApi.recruitExamOperationId,
            "optType": optType
        }
        log.info('test_name={}, url={}, data={}'.
                 format('线上运营启用，禁用，删除接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '线上运营启用，禁用，删除接口)')
        test.assert_text(res['msg'], '成功', '线上运营启用，禁用，删除接口)')

    def add_operation_recruit_exam_one(self):
        """线上运营添加接口"""
        api = '/admin-recruitexam/addOperationRecruitExamOne'
        body = {
            "recruitExamId": ReceiveApi.recruitExamId,
            "activityEntityId": 43,
            "recruitStageKey": 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('线上运营添加接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '线上运营添加接口)')
        test.assert_text(res['msg'], '成功', '线上运营添加接口)')

    def get_material_list(self):
        """获取素材列表"""
        api = '/admin-recruitexam/getMaterialList'
        body = {
            "recruitExamId": ReceiveApi.recruitExamId,
            "targetType": 1,
            "recruitStageKey": 1,
            "activityEntityId": 43,
            "page": 1,
            'pageSize': 10
        }
        log.info('test_name={}, url={}, data={}'.
                 format('获取素材列表', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '获取素材列表)')
        test.assert_text(res['msg'], '成功', '获取素材列表)')

    def add_material_one(self):
        """添加绑定素材"""
        api = '/admin-recruitexam/addMaterialOne'
        body = {
            "recruitExamId": ReceiveApi.recruitExamId,
            "attachment": "https://all-imags.oss-cn-hangzhou.aliyuncs.com/jiaoshipai/processApply/2021-04/20210425093421669.pdf",
            "title": "素材名称",
            "targetType": 1,
            "targetId": 1,
            "recruitStageKey": 1,
            "activityEntityId": 43
        }
        log.info('test_name={}, url={}, data={}'.
                 format('添加绑定素材', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '添加绑定素材)')
        test.assert_text(res['msg'], '成功', '添加绑定素材)')
        ReceiveApi.recruitExamMaterialId =  res['data']['recruitExamMaterialId']

    def set_material_one(self):
        """编辑绑定素材"""
        api = '/admin-recruitexam/setMaterialOne'
        body = {
            "recruitExamMaterialId": ReceiveApi.recruitExamMaterialId,
            "attachment": "https://all-imags.oss-cn-hangzhou.aliyuncs.com/jiaoshipai/processApply/2021-04/20210425093421669.pdf",
            "title": "素材名称001",
            'targetType': 1,
            'targetId': 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('编辑绑定素材', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '编辑绑定素材)')
        test.assert_text(res['msg'], '成功', '编辑绑定素材)')

    def opt_material_one(self):
        """删除绑定素材"""
        api = '/admin-recruitexam/optMaterialOne'
        body = {
            "recruitExamMaterialId": ReceiveApi.recruitExamMaterialId,
            "optType": 1,
        }
        log.info('test_name={}, url={}, data={}'.
                 format('删除绑定素材', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '删除绑定素材)')
        test.assert_text(res['msg'], '成功', '删除绑定素材)')

    def get_qrcode_list(self):
        """后台获取推广码列表"""
        api = '/admin-recruitexam/getQrcodeList'
        body = {
            "recruitExamId": ReceiveApi.recruitExamId,
            "recruitStageKey": 1,
            "activityEntityId": "1",
            "channelId": "1",
            "promoter": "160",
            "page": 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('后台获取推广码列表', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '后台获取推广码列表)')
        test.assert_text(res['msg'], '成功', '后台获取推广码列表)')

    def get_wechat_account_list(self):
        """获取公众号列表"""
        api = '/admin-wechat/getWechatAccountList'
        body = {
            "businessId": 1,
            "accountType": 1,
        }
        log.info('test_name={}, url={}, data={}'.
                 format('获取公众号列表', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '获取公众号列表)')
        test.assert_text(res['msg'], '获取成功', '获取公众号列表)')

    def create_qrcode(self):
        """生成小程序带参数二维码"""
        api = '/admin-wechat/createQrcode'
        body = {
            "businessId": 1,
            "waId": "43",
            "recruitExamId": ReceiveApi.recruitExamId,
            "recruitStageKey": 1,
            "activityEntityId": "1",
            "channelId": "1",
            "channelName": "渠道名称001",
            "promoter": "推广人001",
            "sence": "test",
            "senceStart": 1,
            "senceEnd": 10,
            "viewUrl": "pages/index/index",
            "width": 430,
            "isHyaline": 1
        }
        log.info('test_name={}, url={}, data={}'.
                 format('生成小程序带参数二维码', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '生成小程序带参数二维码)')
        test.assert_text(res['msg'], '生成成功', '生成小程序带参数二维码)')

    def add_operate_position_one(self,):
        """运营位添加接口"""
        api = '/admin-recruitexam/addOperatePositionOne'
        body = {
            "activityEntityId": 46,
            "positionCode": "test_1",
            "positionName": '测试',
            "positionDesc": '测试说明'
        }
        log.info('test_name={}, url={}, data={}'.
                 format('运营位添加接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '运营位添加接口)')
        test.assert_text(res['msg'], '成功', '运营位添加接口)')
        try:
            ReceiveApi.positionId = res['data']['positionId']
        except :
            pass

    def set_operate_position_one(self):
        """运营位修改接口"""
        api = '/admin-recruitexam/setOperatePositionOne'
        body = {
            "positionId": ReceiveApi.positionId,
            'activityEntityId': 46,
            "positionCode": "test_1",
            "positionName": '测试001',
            "positionDesc": '测试说明'
        }
        log.info('test_name={}, url={}, data={}'.
                 format('运营位修改接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '运营位修改接口)')
        test.assert_text(res['msg'], '成功', '运营位修改接口)')

    def get_operate_position_one(self):
        """运营位查询接口"""
        api = '/admin-recruitexam/getOperatePositionOne'
        body = {
            "positionId": ReceiveApi.positionId
        }
        log.info('test_name={}, url={}, data={}'.
                 format('运营位查询接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '运营位查询接口)')
        test.assert_text(res['msg'], '成功', '运营位查询接口)')

    def get_operate_position_list(self, positionType):
        """运营位列表接口"""
        api = '/admin-recruitexam/getOperationPositionList'
        body = {
            "positionType": positionType,
            'page': 1,
            'pageSize': 10,
            'activityEntityId': 46,
            'positionName': '测试001'
        }
        log.info('test_name={}, url={}, data={}'.
                 format('运营位列表接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '运营位列表接口)')
        test.assert_text(res['msg'], '成功', '运营位列表接口)')

    def set_operation_position_0ne(self, positionType):
        """运营位删除接口"""
        api = '/admin-recruitexam/setOperationPositionOne'
        body = {
            "positionType": positionType,
            'positionId': ReceiveApi.positionId
        }
        log.info('test_name={}, url={}, data={}'.
                 format('运营位删除接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '运营位删除接口)')
        test.assert_text(res['msg'], '成功', '运营位删除接口)')

    def get_preset_position_one(self):
        """获取预置位单条接口"""
        api = '/admin-recruitexam/getPresetPositionOne'
        body = {
            'positionId': ReceiveApi.positionId
        }
        log.info('test_name={}, url={}, data={}'.
                 format('获取预置位单条接口', api, body, self.h))
        res = requests.post(url=self.url + api, headers=self.h, data=body)
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '获取预置位单条接口)')
        test.assert_text(res['msg'], '成功', '获取预置位单条接口)')

    def add_preset_position_one(self):
        """预置位添加接口"""
        api = '/admin-recruitexam/addPresetPositionOne'
        h = {
            "token": self.token,
            "Content-Type": "application/json"
        }
        body = {
            "activityEntityId": 46,
            "positionCode": "test",
            "positionName": "首页气泡",
            "templateList": [{
                "templateName": "首页气泡",
                "content": "222222222222",
                "contentFormat": "JSON"
            }]
        }
        log.info('test_name={}, url={}, data={}'.
                 format('预置位添加接口', api, json.dumps(body), self.h))
        res = requests.post(url=self.url + api, headers=h, data=json.dumps(body))
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '预置位添加接口)')
        test.assert_text(res['msg'], '成功', '预置位添加接口)')
        try:
            ReceiveApi.positionId = res['data']['positionId']
        except :
            pass

    def set_preset_position_one(self):
        """预置位编辑接口"""
        api = '/admin-recruitexam/setPresetPositionOne'
        h = {
            "token": self.token,
            "Content-Type": "application/json"
        }
        body = {
            "activityEntityId": 46,
            "activityEntityName": "职位查询小程序",
            "positionCode": "test01",
            "positionDesc": "",
            "positionId": ReceiveApi.positionId,
            "positionName": "首页气泡001",
            "positionType": 1,
            "templateList": [{
                "content": "222222222222",
                "contentFormat": "JSON",
                "templateId": 174,
                "templateName": "首页气泡"
            }]
        }
        log.info('test_name={}, url={}, data={}'.
                 format('预置位编辑接口', api, json.dumps(body), self.h))
        res = requests.post(url=self.url + api, headers=h, data=json.dumps(body))
        res = res.json()
        log.info('响应结果：%s' % res)
        test.assert_text(res['code'], 1, '预置位编辑接口)')
        test.assert_text(res['msg'], '成功', '预置位编辑接口)')


