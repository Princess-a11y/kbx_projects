import allure
import logging
import requests
import pymysql

# --------http请求
@allure.step("2.发送请求的响应")
def send_http_requests(**requests_data):
    res = requests.request(**requests_data)
    logging.info(f"2.发送http请求的响应:{res.text}")
    return res

# --------sql请求
def send_sql_requests(sql,index = 0):
    # 连接数据库
    from config.config_环境配置 import mysql_host, mysql_port, mysql_user, mysql_password, mysql_database
    con = pymysql.connect(
        host=mysql_host,
        port=mysql_port,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database,
        charset="utf8"
    )
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    con.close()
    return result[index]





