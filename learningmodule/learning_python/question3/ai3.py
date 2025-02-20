import sqlite3
import csv
import zipfile
import os

def get_all_table_names(conn):
    """
    获取数据库中所有表的名称
    :param conn: 数据库连接对象
    :return: 包含所有表名的列表
    """
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
    return [table[0] for table in cursor.fetchall()]

def export_table_to_csv(conn, table_name):
    """
    将指定表的数据导出为 CSV 文件
    :param conn: 数据库连接对象
    :param table_name: 表名
    """
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    # 获取表头
    headers = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    try:
        with open(f'{table_name}.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # 写入表头
            writer.writerow(headers)
            # 写入数据行
            writer.writerows(rows)
        print(f'{table_name}.csv 文件导出成功。')
    except Exception as e:
        print(f'导出 {table_name}.csv 文件时出现错误: {e}')

def zip_csv_files(csv_files, zip_file_name):
    """
    将多个 CSV 文件打包成一个 ZIP 文件
    :param csv_files: 包含 CSV 文件路径的列表
    :param zip_file_name: ZIP 文件的名称
    """
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for csv_file in csv_files:
                if os.path.exists(csv_file):
                    zipf.write(csv_file)
        print(f'{zip_file_name} 文件打包成功。')
    except Exception as e:
        print(f'打包 {zip_file_name} 文件时出现错误: {e}')

def backup_database():
    """
    备份数据库中的所有表数据到 CSV 文件并打包成 ZIP 文件
    """
    try:
        # 连接到数据库
        conn = sqlite3.connect('example.db')
        # 获取所有表名
        table_names = get_all_table_names(conn)
        csv_files = []

        # 导出每个表的数据为 CSV 文件
        for table_name in table_names:
            export_table_to_csv(conn, table_name)
            csv_files.append(f'{table_name}.csv')

        # 关闭数据库连接
        conn.close()

        # 打包所有 CSV 文件为 ZIP 文件
        zip_csv_files(csv_files, 'database_backup.zip')

        # 删除临时的 CSV 文件
        for csv_file in csv_files:
            if os.path.exists(csv_file):
                os.remove(csv_file)
        print('临时 CSV 文件已删除。')
    except Exception as e:
        print(f'备份数据库时出现错误: {e}')

if __name__ == '__main__':
    backup_database()