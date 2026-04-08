import allure


def allure_init(case):
    # 初始化 allure 报告
    allure.dynamic.feature(case.get("feature"))
    allure.dynamic.story(case.get("story"))

    # 修正点：外层用双引号，内部变量取值用单引号，防止冲突
    allure.dynamic.title(f"ID:{case.get('id')}--{case.get('title')}")