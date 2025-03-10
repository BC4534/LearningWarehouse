import pandas as pd
import re

# 读取 txt 文件内容
with open('户外柜国际化.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# 读取 Excel 文件
excel_file = pd.ExcelFile('old_data/翻译词条汇总.xlsx')

# 定义要处理的工作表名称
sheet_names = ['前端词条汇总', '运维系统前端词条（禁止编辑）', '后端词条汇总', 'EMS-鹰普告警字段汇总（禁止编辑）']

# 定义预处理函数，去除符号并将英文转小写
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', str(text))
    text = text.lower()
    return text

# 遍历每个工作表
for sheet_name in sheet_names:
    df = excel_file.parse(sheet_name)
    df['processed_col_A'] = df.iloc[:, 0].apply(preprocess_text)
    # 遍历 txt 文件的每一行
    for i, line in enumerate(lines):
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            # 预处理 txt 中的值
            processed_value = preprocess_text(value)
            # 先尝试整体匹配
            match = df[df['processed_col_A'] == processed_value]
            if not match.empty:
                new_value = match.iloc[0, 1]
                lines[i] = f"{key}={new_value}\n"
            else:
                # 若整体匹配失败，尝试拆分匹配
                pattern = r'[()]'
                sub_values = re.split(pattern, value)
                sub_translations = []
                all_matched = True
                for sub_value in sub_values:
                    sub_value = sub_value.strip()
                    if sub_value:
                        processed_sub_value = preprocess_text(sub_value)
                        sub_match = df[df['processed_col_A'] == processed_sub_value]
                        if not sub_match.empty:
                            sub_translations.append(sub_match.iloc[0, 1])
                        else:
                            all_matched = False
                            break
                if all_matched and sub_translations:
                    # 若拆分后的部分都匹配到，合并翻译结果
                    combined_translation = ' '.join(sub_translations)
                    lines[i] = f"{key}={combined_translation}\n"

# 将修改后的内容写回 txt 文件
with open('old_data/户外柜国际化_replace3.0.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(lines)