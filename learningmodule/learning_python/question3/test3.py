# 题目 15：数据库数据备份
# 假设你使用的是 SQLite 数据库，数据库文件名为 example.db，其中包含多个表。编写一个 Python 程序，完成以下任务：
import sqlite3
import csv
# 连接到 example.db 数据库。
conn = sqlite3.connect('example.db')
curs = conn.cursor()
# 遍历数据库中的所有表。
select_all_tabel='select name from sqlite_master where type = "table"'
curs.execute(select_all_tabel)
name_list = []
select_table = "select * from "
for table in curs.fetchall():
    name_list.append(list(table))
    curs.execute(select_table+f'{table[0]}')
# 对于每个表，将表中的数据导出为 CSV 文件，文件名以表名命名，例如 table_name.csv。
    with open(f'{table[0]}.csv','w',encoding='utf-8') as f:
        for line in curs.fetchall():
            writer = csv.writer(f)
            writer.writerow(line)
# 将所有导出的 CSV 文件打包成一个 ZIP 文件，名为 database_backup.zip
file_list = []
for name in name_list:
    file_list.append(str(name[0])+".csv")
import zipfile
with zipfile.ZipFile('database_backup.zip','w',zipfile.ZIP_DEFLATED) as zipf:
    for file in file_list:
        zipf.write(file)




