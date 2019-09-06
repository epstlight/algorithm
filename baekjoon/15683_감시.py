import sys, copy
#  오른쪽 왼쪽 아래 위
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def is_wall(xx, yy):
    if xx >= 0 and yy >= 0 and xx < m and yy < n: return False
    else: return True

def cnt_notsee(office):
    zero_cnt = 0
    cctv_map = copy.deepcopy(office)

    for y in range(n):
        for x in range(m):
            if type(cctv_map[y][x]) == tuple:
                number, direc = cctv_map[y][x]
                if number < 6:
                    xx, yy = x + dx[direc], y + dy[direc] # 0
                    while not is_wall(xx, yy) and cctv_map[yy][xx] != 6:
                        if cctv_map[yy][xx] == 0: cctv_map[yy][xx] = -1
                        xx, yy = xx + dx[direc], yy + dy[direc]

                if number == 2 or number == 4 or number == 5:
                    if direc == 0 or direc == 2: #0 -> 1, 2 => 3
                        temp_direc = direc + 1
                    else:
                        temp_direc = direc - 1 # 1 -> 0 , 3 -> 2
                    xx, yy = x + dx[temp_direc], y + dy[temp_direc]
                    while not is_wall(xx, yy) and cctv_map[yy][xx] != 6:
                        if cctv_map[yy][xx] == 0: cctv_map[yy][xx] = -1
                        xx, yy = xx + dx[temp_direc], yy + dy[temp_direc]

                if number == 4 or number == 3 or number == 5:
                    if direc == 0: temp_direc = direc + 3  # 0 -> 3
                    elif direc == 1: temp_direc = direc + 1 # 1 -> 2
                    elif direc == 2: temp_direc = direc - 2 # 2 -> 0
                    elif direc == 3: temp_direc = direc - 2 # 3 -> 1

                    xx, yy = x + dx[temp_direc], y + dy[temp_direc]
                    while not is_wall(xx, yy) and cctv_map[yy][xx] != 6:
                        if cctv_map[yy][xx] == 0: cctv_map[yy][xx] = -1
                        xx, yy = xx + dx[temp_direc], yy + dy[temp_direc]

                if number == 5:
                    temp_direc = direc + 2 # 0 -> 2
                    xx, yy = x + dx[temp_direc], y + dy[temp_direc]
                    while not is_wall(xx, yy) and cctv_map[yy][xx] != 6:
                        if cctv_map[yy][xx] == 0: cctv_map[yy][xx] = -1
                        xx, yy = xx + dx[temp_direc], yy + dy[temp_direc]

    for y in range(n):
        for x in range(m):
            if cctv_map[y][x] == 0: zero_cnt += 1
    return zero_cnt


def direc_select(x, y, cnt):
    global min_cnt

    if cnt == cctv_cnt:
        min_cnt = min(min_cnt, cnt_notsee(office_map))
    else:
        for yy in range(y, n):
            k = x if yy == y else 0
            for xx in range(k, m):
                if office_map[yy][xx] > 0 and office_map[yy][xx] < 6:
                    if office_map[yy][xx] == 2:
                        temp = office_map[yy][xx]
                        for i in range(0, 3, 2):
                            office_map[yy][xx] = (temp, i)
                            direc_select(xx + 1, yy, cnt + 1)
                            office_map[yy][xx] = temp

                    elif office_map[yy][xx] == 5:
                        office_map[yy][xx] = (5, 0)
                        direc_select(xx + 1, yy, cnt + 1)
                        office_map[yy][xx] = 5

                    else:
                        temp = office_map[yy][xx]
                        for i in range(4):
                            office_map[yy][xx] = (temp, i)
                            direc_select(xx + 1, yy, cnt + 1)
                            office_map[yy][xx] = temp



n, m = map(int, input().strip().split())
office_map = list(list(map(int, input().strip().split())) for _ in range(n))

cctv_cnt = 0
for y in range(n):
    for x in range(m):
        if office_map[y][x] > 0 and office_map[y][x] < 6: cctv_cnt += 1

min_cnt = sys.maxsize
direc_select(0, 0, 0)
print(min_cnt)