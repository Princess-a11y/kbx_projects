import allure
import logging
from jsonpath_ng import parse

# ----------------jsonExdata提取
def json_ExData(case, all, res):
    if case.get("jsonExData"):
        with allure.step("5.json提取"):
            for key, path_str in eval(case.get("jsonExData")).items():
                # 解析并提取数据
                value = parse(path_str).find(res.json())[0].value
                all[key] = value

        # 增加了日志：打印提取的变量名、路径和结果
        logging.info(f'5.json提取，根据{case.get("jsonExData")}提取数据，此时全局变量为:{all}')

# ----------------sqlExdata提取
def sql_ExData(case, all, res):
    if case.get("sqlExData"):
        with allure.step("6.sql提取"):
            for key, value in eval(case.get("sqlExData")).items():
                from utils.requests_utils import send_sql_requests
                db_value = send_sql_requests(value)
                # 兼容处理
                if isinstance(db_value, (list, dict)) and db_value:
                    db_value = list(db_value.values())[0] if isinstance(db_value, dict) else db_value[0]
                all[key] = db_value

        logging.info(f'6.sql提取，根据{case.get("sqlExData")}提取数据，此时全局变量为:{all}')