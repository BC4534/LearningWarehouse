import pandas as pd

# 读取 txt 文件内容
with open('input.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# 读取 Excel 文件
excel_file = pd.ExcelFile('input.xlsx')

# 定义要处理的工作表名称
sheet_names = ['前端词条汇总', '运维系统前端词条（禁止编辑）', '后端词条汇总', 'EMS-鹰普告警字段汇总（禁止编辑）']

# 遍历每个工作表
for sheet_name in sheet_names:
    df = excel_file.parse(sheet_name)
    # 遍历 txt 文件的每一行
    for i, line in enumerate(lines):
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            # 在当前工作表的 A 列中查找匹配的内容
            match = df[df.iloc[:, 0] == value]
            if not match.empty:
                new_value = match.iloc[0, 1]
                lines[i] = f"{key}={new_value}\n"

# 将修改后的内容写回 txt 文件
with open('output.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(lines)