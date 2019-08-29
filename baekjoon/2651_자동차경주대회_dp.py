
limit = int(input().strip())
station_cnt = int(input().strip())
dp_station = [0] * (station_cnt + 2)
station = [0] * (station_cnt + 2)

station_list = [[] for _ in range(station_cnt + 2)]
temp = list(map(int, input().strip().split()))
for i in range(1, station_cnt + 2):
    station[i] = temp[i - 1] + station[i - 1]

station_minute = [0]
station_minute.extend(list(map(int, input().strip().split())))
station_minute.append(0)

start_idx = 0
for i in range(1, station_cnt + 2):
    if station[i] > limit:
        start_idx = i
        break
    else:
        dp_station[i] = station_minute[i]
        station_list[i].append(i)

temp_sequence = []
for i in range(start_idx, station_cnt + 2):
    temp_min = 1000000
    for j in range(i - 1, 0, -1):
        if station[i] - limit <= station[j]:
            if temp_min > dp_station[j]:
                temp_min = dp_station[j]
                temp_sequence = station_list[j][:]
        else: break
    dp_station[i] = temp_min + station_minute[i]
    station_list[i] = temp_sequence[:]
    station_list[i].append(i)


station_list[-1] = station_list[-1][:-1]
if not len(station_list[-1]):
    print(0)
else:
    print(dp_station[-1])
print(len(station_list[-1]))
for num in station_list[-1]:
    print(num, end=' ')