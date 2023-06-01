import json

import requests

from Common.Methodes import Notify
from Common.signature import value_list
from Config.Config import Config


class ProductConfig:

    # 产品管理--分页查询产品配置信息
    @staticmethod
    def page_query_product_config(body, **kwargs):
        """
         :param kwargs: 其他参数
         :return: json格式请求结果

         """
        url = Config().finance_url
        api = f'/admin/product/productConfig/pageQueryProductConfig'

        response = Notify().notify_result(mode=1, url=url + api, header={}, data=body, f_type='json')
        return response
