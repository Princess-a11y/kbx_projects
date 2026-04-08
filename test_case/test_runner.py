import logging
import pytest
import requests
import jsonpath
import pymysql
from jinja2 import Template  # <--- 确保这里导入的是 jinja2
import allure


class TestCase:
    # 读取excel数据，用属性保存
    from utils.excel_utils import read_excel
    data = read_excel()

    # 根据读取后的数据需要初始化一个属性保存，可以用{}
    all = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # 引用全局变量(测试函数内外all，变量的对应）
        all = self.all

        # --- 修改核心代码 ---
        # 使用 jinja2 的 Template，这样 Excel 里用 {{token}} 或 ${token} 都能识别
        case = eval(Template(str(case)).render(all))
        # -------------------

        # 1.调用allure参数
        from utils.allure_utils import allure_init
        allure_init(case=case)

        # 0：测试用例的描述信息日志
        logging.info(
            f"0.用例ID:{case.get('id')} , 模块:{case.get('feature')},场景:{case.get('story')}，标题:{case.get('title')}")

        # 1.调用用例参数
        from utils.testcase_utils import analy_testcase
        requests_data = analy_testcase(case)

        # 调用请求参数，得到响应结果
        from utils.requests_utils import send_http_requests
        res = send_http_requests(**requests_data)

        # ================= 核心步骤3：先断言 =================

        # ----------------Http断言
        from utils.asserts_utils import http_asserts
        http_asserts(case, res)

        # ----------------Sql断言
        from utils.asserts_utils import sql_asserts
        sql_asserts(case, res)

        # ================= 核心步骤4：后提取 =================

        # ----------------jsonExdata提取
        # 引入提取函数
        from utils.ExData_utils import json_ExData
        # 执行提取（把数据存入 self.all）
        json_ExData(case, self.all, res)

        # ----------------sqlExdata提取
        from utils.ExData_utils import sql_ExData
        sql_ExData(case, self.all, res)