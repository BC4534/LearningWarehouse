# # 题目 1：文本文件行数统计
# #
# # 有一个文本文件 `textfile.txt`，编写一个 Python 程序，统计该文件的总行数，并将结果打印输出。
# from idlelib.iomenu import encoding
#
# # with open('textfile.txt', 'r', encoding='utf-8') as f:
# #     lines = f.readlines()
# #     print(len(lines))
# # 有一个文本文件 case.txt，编写 Python 程序将其内容复制到一个新的文件 destination.txt 中。
# # 现在你可以尝试编写代码来解决这个问题，有任何疑问都能随时问我。
# # with open ('case.txt', 'r', encoding='utf-8') as f:
# #     r = f.readlines()
# # for i in r:
# #     with open("destination.txt",'a',encoding="utf-8") as f:
# #         f.write(i)
# # 题目 3：文本文件大小写转换
# # 有一个文本文件 case.txt，编写 Python 程序将文件中的所有小写字母转换为大写字母，所有大写字母转换为小写字母，然后将结果保存到新文件 converted_case.txt 中。
# # with open ('case.txt','r',encoding='utf-8') as f:
# #     lines = f.readlines()
# #     for i,line in enumerate(lines):
# #         # lines[i]=line.lower()
# #         lines[i]=line.swapcase()
# # with open('converted_case.txt','w',encoding='utf-8') as f:
# #     f.writelines(lines)
# # 编写 Python 程序，读取该 JSON 文件，筛选出年龄大于 28 岁的用户
# # 将这些用户信息保存到一个新的 JSON 文件 filtered_data.json 中。同时，计算这些筛选出的用户的平均年龄，并将结果打印输出。
# # import json
# # sum_age = 0
# # sum_people = 0
# # filtered_list = []
# # with open ('data.json','r',encoding='utf-8') as f:
# #     json_list = json.load(f)
# #     for list in json_list:
# #         if list['age']>28:
# #             sum_age += list['age']
# #             sum_people += 1
# #             filtered_list.append(list)
# #
# #
# # with open('filtered_data.json','w',encoding='utf-8') as f:
# #     json.dump(filtered_list,f)
# # avg_age=sum_age/sum_people
# # print(f'平均年龄{avg_age}')
# # 读取该 XML 文件，将出版年份在 2021 年及以后的书籍的作者名字后面添加 (New) 标记。然后将修改后的 XML 内容保存到一个新的 XML 文件 updated_books.xml 中。
# from lxml import etree
#
# from lxml import etree
#
# # 解析 XML 文件
# tree = etree.parse('books.xml')
# root = tree.getroot()
#
# # 遍历 library 下的 book 元素
# for book in root:
#     if book.tag == 'book':
#         year_element = None
#         author_element = None
#         # 遍历 book 下的子元素
#         for child in book:
#             if child.tag == 'year':
#                 year_element = child
#             elif child.tag == 'author':
#                 author_element = child
#
#         if year_element is not None:
#             try:
#                 year = int(year_element.text)
#                 if year >= 2021 and author_element is not None:
#                     author_element.text = author_element.text + ' (New)'
#             except ValueError:
#                 print(f"年份 {year_element.text} 无法转换为整数，跳过此书籍。")
#
# # 将修改后的 XML 内容保存到新文件
# with open('data/updated_books.xml', 'wb') as f:
#     f.write(etree.tostring(tree, pretty_print=True, encoding='utf-8', xml_declaration=True))
#
# 编写一个 Python 程序，读取这个 CSV 文件，完成以下操作：
# 计算每种商品的总销售量和总销售额。
# 找出总销售额最高的商品。
# 将每种商品的统计结果（商品名称、总销售量、总销售额）保存到一个新的 CSV 文件 sales_summary.csv 中。
import csv
from traceback import print_tb
from webbrowser import open_new

# csv_read = csv.reader(open('sales_data.csv',encoding='utf-8'))
#
# tem = {}
# for i in csv_read:
#     fruit = i[1]
#     sales_volume = int(i[2])
#     unit_price = int(i[3])
#     sales_amount = sales_volume * unit_price
#     if fruit not in tem.keys():
#         tem[fruit] = {'总销售量':sales_volume,'总销售额':sales_amount}
#     else:
#         tem[fruit]['总销售量']=tem[fruit]['总销售量']+sales_volume
#         tem[fruit]['总销售额']=tem[fruit]['总销售额']+sales_amount
#
#
# with open('sales_summary.csv','w',encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['商品名称','总销售量','总销售额'])
#     for key in tem.keys():
#         name = key
#         zxl = tem[key]['总销售量']
#         zxe = tem[key]['总销售额']
#         writer.writerow([f'{name}',f'{zxl}',f'{zxe}'],)

import csv

# 初始化一个空字典，用于存储每种商品的统计信息
# product_stats = {}

# 读取销售数据 CSV 文件
# with open('data/sales_data.csv', 'r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     # 跳过标题行
#     next(csv_reader)
#     for row in csv_reader:
#         product_name = row[1]
#         sales_volume = int(row[2])
#         unit_price = int(row[3])
#         sales_amount = sales_volume * unit_price
#
#         if product_name not in product_stats:
#             product_stats[product_name] = {
#                 'total_sales_volume': sales_volume,
#                 'total_sales_amount': sales_amount
#             }
#         else:
#             product_stats[product_name]['total_sales_volume'] += sales_volume
#             product_stats[product_name]['total_sales_amount'] += sales_amount
#
# # 找出总销售额最高的商品
# max_sales_amount_product = None
# max_sales_amount = 0
# for product, stats in product_stats.items():
#     if stats['total_sales_amount'] > max_sales_amount:
#         max_sales_amount = stats['total_sales_amount']
#         max_sales_amount_product = product
#
# print(f"总销售额最高的商品是: {max_sales_amount_product}，总销售额为: {max_sales_amount}")
#
# # 将每种商品的统计结果保存到新的 CSV 文件中
# with open('data/sales_summary.csv', 'w', encoding='utf-8', newline='') as file:
#     csv_writer = csv.writer(file)
#     # 写入标题行
#     csv_writer.writerow(['商品名称', '总销售量', '总销售额'])
#     for product, stats in product_stats.items():
#         csv_writer.writerow([product, stats['total_sales_volume'], stats['total_sales_amount']])



# 请编写一个 Python 程序，完成以下任务：
# 读取 app.log 文件，统计每种日志级别的出现次数。
# 找出出现次数最多的日志级别。
# 提取所有 ERROR 级别的日志，并将这些日志保存到一个新的文件 error_logs.log 中。
# 读取所有日志信息
import re
with open('app.log', 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()
# 创建一个字典，存储日志出现次数
log_num = {}
error_log = ""
for line in lines:
    level = re.search(r'[A-Z]+',line).group()
    if level == 'ERROR':
        error_log = error_log+line+'\n'
    elif level not in log_num.keys():
        log_num[level] = 1
    else:
        log_num[level] +=1
with open('error_logs.log', 'a', encoding='utf-8') as f:
    f.writelines(error_log)
m = max(log_num.values())
for k in log_num.keys():
    if log_num[k] == m:
        print(f'出现日志最多的是{k}，出现了{m}次')

