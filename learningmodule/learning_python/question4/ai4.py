import csv
from datetime import datetime, timedelta

def read_csv(file):
    """
    读取 CSV 文件内容
    :param file: CSV 文件路径
    :return: 包含 CSV 文件内容的列表
    """
    try:
        csv_list = []
        with open(file, 'r', encoding='utf-8') as f:
            readers = csv.reader(f)
            for row in readers:
                csv_list.append(row)
        return csv_list
    except FileNotFoundError:
        print(f"错误：未找到文件 {file}。")
        return []

def count_flight_city_num(csv_list):
    """
    统计每个出发城市的航班数量
    :param csv_list: 包含航班信息的列表
    :return: 包含每个出发城市航班数量的字典
    """
    city_num = {}
    for row in csv_list[1:]:
        departure_city = row[1]
        if departure_city not in city_num:
            city_num[departure_city] = 1
        else:
            city_num[departure_city] += 1
    return city_num

def find_max_price(csv_list):
    """
    找出票价最高的航班信息
    :param csv_list: 包含航班信息的列表
    :return: 票价最高的航班信息列表
    """
    max_price = 0
    max_flight = None
    for row in csv_list[1:]:
        price = int(row[5])
        if price > max_price:
            max_price = price
            max_flight = row
    return max_flight

def avg_flight_time(csv_list):
    """
    计算所有航班的平均飞行时长（以小时为单位）
    :param csv_list: 包含航班信息的列表
    :return: 所有航班的平均飞行时长（小时）
    """
    total_flight_time = timedelta(0)
    num_flights = len(csv_list) - 1
    for row in csv_list[1:]:
        departure_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
        arrival_time = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
        flight_time = arrival_time - departure_time
        total_flight_time += flight_time
    if num_flights > 0:
        return total_flight_time.total_seconds() / 3600 / num_flights
    return 0

def format_max_flight_info(max_flight):
    """
    格式化票价最高的航班信息
    :param max_flight: 票价最高的航班信息列表
    :return: 格式化后的航班信息字符串
    """
    flight_id, departure_city, arrival_city, departure_time, arrival_time, price = max_flight
    return f"{flight_id}: {departure_city} -> {arrival_city}, 出发时间: {departure_time}, 到达时间: {arrival_time}, 票价: {price}"

def write_resout():
    """
    将统计结果保存到文本文件中
    """
    csv_list = read_csv('flights.csv')
    if not csv_list:
        return
    city_num = count_flight_city_num(csv_list)
    max_flight = find_max_price(csv_list)
    avg_time = avg_flight_time(csv_list)

    try:
        with open('flight_analysis.txt', 'w', encoding='utf-8') as f:
            f.write('每个出发城市的航班数量：\n')
            for city, num in city_num.items():
                f.write(f'{city}: {num}\n')
            f.write('\n票价最高的航班信息：\n')
            f.write(format_max_flight_info(max_flight) + '\n')
            f.write(f'\n所有航班的平均飞行时长：{avg_time:.2f} 小时')
        print("统计结果已成功保存到 flight_analysis.txt 文件中。")
    except Exception as e:
        print(f"写入文件时出现错误：{e}")

if __name__ == '__main__':
    write_resout()