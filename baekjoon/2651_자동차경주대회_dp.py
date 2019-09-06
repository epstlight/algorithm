#다시 풀어보기
limit = int(input().strip())
station_cnt = int(input().strip())
station_list = [0] * (station_cnt+1)
station_minute = [0] * (station_cnt+1)
dp_list = [[0, 0, []] for _ in range(station_cnt+2)]

station_list[1:] = map(int, input().strip().split())
station_minute[1:-1] = map(int, input().strip().split())

for i in range(1, len(station_list)):
    station_list[i] += station_list[i - 1]

for i in range(1, len(station_list)):
    if station_list[i] - limit <= 0:
        dp_list[i][0] = station_minute[i]   # minite
        dp_list[i][1] = 1                   # cnt
        dp_list[i][2].append(i)       #순서
    else:
        temp_idx = i
        for j in range(i - 1, 0, -1):
            if station_list[i] - limit <= station_list[j]:
                temp_idx = j
            else: break
        temp_list = sorted(dp_list[temp_idx:i], key=lambda x:x[0])
        # print(temp_list)
        dp_list[i][0] = temp_list[0][0] + station_minute[i]
        dp_list[i][1] = temp_list[0][1] + 1
        dp_list[i][2] = temp_list[0][2][:]
        dp_list[i][2].append(i)

if limit >= station_list[-1]:
    print(0)
    print(0)
else:
    print(dp_list[-1][0])
    print(dp_list[-1][1]-1)
    for num in dp_list[-1][2][:-1]: print(num, end=' ')

