import openpyxl

from config.config_环境配置 import excel_file
from config.config_环境配置 import sheet_name

def read_excel(file_load=excel_file,sheet=sheet_name):
    # 打开 Excel 表
    workbook = openpyxl.load_workbook(file_load,sheet)

    # 选择表
    sheet = workbook["Sheet1"]

    # 读取数据（第三行及以后）
    data = []
    keys = [cell.value for cell in sheet[2] if cell.value is not None]
    for row in sheet.iter_rows(min_row=3, values_only=True):
        dict_data = dict(zip(keys, row))
        # 如果读取的is_true 字段的值是ture，则apped，否则 不apped
        if dict_data["is_true"]:
         data.append(dict_data)
        # print(dict_data)
        # print(data)

    # 关闭 Excel 文件
    workbook.close()
    return data

# read_excel()

