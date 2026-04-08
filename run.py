import os
import pytest

if __name__ == "__main__":
    # 1. 执行测试
    pytest.main([
        "-vs",
        "./test_case/test_runner.py",
        "--alluredir=./report/json_report",
        "--clean-alluredir"
    ])

    # 2. 生成报告 (直接执行命令)
    os.system(r'"D:\python项目\allure-2.35.1\bin\allure.bat" generate ./report/json_report -o ./report/html_report --clean')



