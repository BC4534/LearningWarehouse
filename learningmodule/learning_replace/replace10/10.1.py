import pandas as pd

# 读取 txt 文件内容
with open('户外柜国际化.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# 读取 Excel 文件
excel_file = pd.ExcelFile('翻译词条汇总.xlsx')

# 定义要处理的工作表名称
sheet_names = ['前端词条汇总', '运维系统前端词条（禁止编辑）', '后端词条汇总', 'EMS-鹰普告警字段汇总（禁止编辑）']

# 存储不同匹配情况的词条
fully_matched_lines = []
unmatched_lines = []

# 遍历 txt 文件的每一行
for i, line in enumerate(lines):
    parts = line.strip().split('=')
    if len(parts) == 2:
        key, value = parts
        # 标记是否匹配成功
        is_matched = False

        # 遍历每个工作表进行匹配
        for sheet_name in sheet_names:
            df = excel_file.parse(sheet_name)
            # 直接尝试整体匹配
            match = df[df.iloc[:, 0] == value]
            if not match.empty:
                new_value = match.iloc[0, 1]
                new_line = f"{key}={new_value}\n"
                lines[i] = new_line
                fully_matched_lines.append(new_line)
                is_matched = True
                break

        # 如果匹配失败，将该词条添加到未匹配列表
        if not is_matched:
            unmatched_lines.append(line)

# 将修改后的内容写回总 txt 文件
with open('户外柜国际化_替换.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(lines)

# 将完全匹配上的词条写入新的 txt 文件
with open('户外柜国际化_完全匹配.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(fully_matched_lines)

# 将匹配不上的词条写入新的 txt 文件
with open('户外柜国际化_不匹配.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(unmatched_lines)