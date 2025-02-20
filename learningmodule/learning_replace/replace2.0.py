import pandas as pd
import re

# 定义一个函数来预处理文本，去除符号并将英文转小写
def preprocess_text(text):
    # 去除中英文标点符号
    text = re.sub(r'[^\w\s]', '', str(text))
    # 将英文转换为小写
    text = text.lower()
    return text

# 读取 txt 文件内容
with open('户外柜国际化.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# 读取 Excel 文件
excel_file = pd.ExcelFile('old_data/翻译词条汇总.xlsx')

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
            # 对 txt 中的值进行预处理
            processed_value = preprocess_text(value)
            # 在当前工作表的 A 列中查找匹配的内容（经过预处理）
            df['processed_col_A'] = df.iloc[:, 0].apply(preprocess_text)
            match = df[df['processed_col_A'] == processed_value]
            if not match.empty:
                new_value = match.iloc[0, 1]
                lines[i] = f"{key}={new_value}\n"

# 将修改后的内容写回 txt 文件
with open('old_data/户外柜国际化_replace2.0.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(lines)