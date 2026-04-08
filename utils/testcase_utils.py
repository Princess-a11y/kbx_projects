import allure
import logging
import json


@allure.step("1.解析请求数据")
def analy_testcase(case):
    # 1. 获取请求方法
    method = case.get("method")

    # 2. 拼接完整 URL
    from config.config_环境配置 import BASE_URL
    url = BASE_URL + case.get("path", "")

    # 3. 处理请求参数
    headers = eval(case.get("headers")) if case.get("headers") and str(case.get("headers")).strip() else None
    params = eval(case.get("params")) if case.get("params") and str(case.get("params")).strip() else None
    data_body = eval(case.get("data")) if case.get("data") and str(case.get("data")).strip() else None


    # --- 使用 eval 解析字典 ---
    files = eval(case.get("files")) if case.get("files") and str(case.get("files")).strip() else None

    # JSON 处理
    json_raw = case.get("json")
    json_data = json.loads(json_raw) if json_raw and str(json_raw).strip() else None

    # 4. 组装
    requests_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data_body,
        "json": json_data,
        "files": files
    }

    logging.info(f"1.解析请求数据，请求数据为:{requests_data}")
    allure.attach(f"{requests_data}", name="解析数据结果")

    return requests_data


