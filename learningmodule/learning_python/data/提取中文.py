import re
import pandas as pd

# 读取文本文件
file_path = '户外柜国际化_不匹配7.7.txt'  # 替换为实际的文本文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 定义正则表达式模式，用于匹配中文及括号
pattern = re.compile(r'[\u4e00-\u9fa5()]+')

# 用于存储不重复的中文部分
unique_chinese_parts = set()
for line in lines:
    matches = pattern.findall(line)
    if matches:
        chinese_text = ''.join(matches)
        unique_chinese_parts.add(chinese_text)

# 将集合转换为列表，以便创建 DataFrame
chinese_parts_list = list(unique_chinese_parts)

# 创建 DataFrame
df = pd.DataFrame(chinese_parts_list, columns=['中文内容'])

# 保存到 Excel 文件
excel_path = '没有翻译字段.xlsx'  # 输出的 Excel 文件路径
df.to_excel(excel_path, index=False)

print(f'已将不重复的中文内容提取并保存到 {excel_path} 文件中。')