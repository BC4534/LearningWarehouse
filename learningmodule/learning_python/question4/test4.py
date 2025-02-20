# 请编写一个 Python 程序，完成以下任务：
# 读取 flights.csv 文件内容。
# 统计每个出发城市的航班数量。
# 找出票价最高的航班信息。
# 计算所有航班的平均飞行时长（以小时为单位）。
# 将统计结果保存到一个新的文本文件 flight_analysis.txt 中，格式如下：
import csv
from datetime import datetime, timedelta


def read_csv(file):
    csv_list = []
    with open(file,'r',encoding='utf-8') as f:
        readers = csv.reader(f)
        for read in readers:
            csv_list.append(read)
    return csv_list
def count_flight_city_num(csv_list:list):
    city_num = {}
    max_price = 0
    for i in range(1,len(csv_list)):
        if csv_list[i][1] not in city_num.keys():
            city_num[csv_list[i][1]] = 1

        else:
            city_num[csv_list[i][1]] += 1
    return city_num
def find_max_price(csv_list):
    max_price = 0
    max_i = 0
    for i in range(1, len(csv_list)):
        if max_price < int(csv_list[i][5]):
            max_price = int(csv_list[i][5])
            max_i = i
    print( f'票价最高的是{max_price},flight_id={max_i}')
    return max_i

def avg_flight_time(csv_list):
    sum_id = 0
    sum_flight_time = timedelta(0)
    for i in range(1, len(csv_list)):
        departure_time = datetime.strptime(csv_list[i][3], "%Y-%m-%d %H:%M:%S")
        arrival_time = datetime.strptime(csv_list[i][4], "%Y-%m-%d %H:%M:%S")
        sum_id += 1
        sum_flight_time = sum_flight_time + (arrival_time-departure_time)
    print(f'平均飞行时长{sum_flight_time/sum_id}')
    return sum_flight_time/sum_id
# 每个出发城市的航班数量：
# <出发城市 1>: <航班数量 1>
# <出发城市 2>: <航班数量 2>
# ...
#
# 票价最高的航班信息：
# <航班编号>: <出发城市> -> <到达城市>, 出发时间: <出发时间>, 到达时间: <到达时间>, 票价: <票价>
#
# 所有航班的平均飞行时长：<平均飞行时长> 小时
def write_resout():
    csv_list = read_csv('flights.csv')
    id = find_max_price(csv_list)
    city_num = count_flight_city_num(csv_list)
    time = avg_flight_time(csv_list)
    with open('flight_analysis.txt','w',encoding='utf-8') as f:
        f.write('每个出发城市的航班数量：\n')
        for key in city_num.keys():
            f.write(f'{key}:{city_num[key]}\n')
        f.write(f'票价最高的航班信息：\n')
        x = 1
        for i in csv_list[id]:
            x +=1
            f.write(i)
            if x == len(csv_list[id]):
                f.write('\n')
            else:
                f.write(',')

        f.write(f'所有航班的平均飞行时长：{time} 小时')






if __name__ == '__main__':
    # csv_list = read_csv('flights.csv')
    # city_num = count_flight_city_num(csv_list)
    # print(city_num)
    # find_max_price(csv_list)
    # avg_flight_time(csv_list)
    write_resout()
