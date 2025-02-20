import pandas as pd

# 读取文本文件
file_path = '户外柜国际化_不匹配.txt'  # 请将此替换为你的实际文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 存储 = 前后的内容
keys = []
values = []

# 遍历每一行，提取 = 前后的内容
for line in lines:
    line = line.strip()
    if '=' in line:
        key, value = line.split('=', 1)
        keys.append(key)
        values.append(value)

# 创建 DataFrame
data = {
    '键': keys,
    '值': values
}
df = pd.DataFrame(data)

# 将 DataFrame 保存到 Excel 文件
output_file = 'output.xlsx'
df.to_excel(output_file, index=False)

print(f"提取的内容已保存到 {output_file} 文件中。")