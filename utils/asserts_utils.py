import allure
import logging
from jsonpath_ng import parse


@allure.step("3.http响应断言")
def http_asserts(case, res):
    check_path = case.get("check")
    expected_val = case.get("expected")

    if check_path:
        logging.info('3.http断言')
        # 直接拆分并遍历，去除多余中间变量
        for path, exp in zip(check_path.split(','), str(expected_val).split(',')):
            path, exp = path.strip(), exp.strip()

            # 获取实际值
            matches = parse(path).find(res.json())
            actual = matches[0].value if matches else None

            logging.info(f'  -> 校验字段: [{path}], 实际值: [{actual}], 预期值: [{exp}]')

            # 核心修改：统一转小写比对，解决 True/true 不一致问题
            assert str(actual).lower() == exp.lower()

    else:
        # 模糊断言
        logging.info(f"3.Http响应断言(模糊): 预期({expected_val}) in 实际({res.text})")
        assert expected_val in res.text


def sql_asserts(case, res):
    if case.get("sql_check") and case.get("sql_expected"):
        from utils.requests_utils import send_sql_requests
        with allure.step("4.sql响应断言"):
            actual_sql_res = send_sql_requests(case.get("sql_check"))
            logging.info(f'4.sql断言: 实际({actual_sql_res}) == 预期({case.get("sql_expected")})')
            assert actual_sql_res == case.get("sql_expected")