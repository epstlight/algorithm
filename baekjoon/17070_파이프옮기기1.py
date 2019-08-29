#벽 1

def horizontal(sx, sy, ex, ey):
    cnt = 0
    sx, ex = ex, ex + 1
    if ex < n and ey < n and not map_list[ey][ex]:
        if ex == n-1 and ey == n-1: cnt += 1
        else: dfs_list.append((0, sx, sy, ex, ey))
    ey += 1
    if ex < n and ey < n and not map_list[ey][ex] and not map_list[ey-1][ex] and not map_list[ey][ex-1]:
        if ex == n-1 and ey == n-1: cnt += 1
        else: dfs_list.append((2, sx, sy, ex, ey))
    # print('horizontal')
    # print(dfs_list)
    return cnt

def vertical(sx, sy, ex, ey):
    cnt = 0

    sy, ey = ey, ey + 1
    if ex < n and ey < n and not map_list[ey][ex]:
        if ex == n - 1 and ey == n - 1: cnt += 1
        else: dfs_list.append((1, sx, sy, ex, ey))
    ex += 1
    if ex < n and ey < n and not map_list[ey][ex] and not map_list[ey-1][ex] and not map_list[ey][ex-1]:
        if ex == n - 1 and ey == n - 1: cnt += 1
        else: dfs_list.append((2, sx, sy, ex, ey))
    # print('vertical')
    # print(dfs_list)
    return cnt


def diagonal(sx, sy, ex, ey):
    cnt = 0
    sx, sy, ex, ey = ex, ey, ex + 1, ey + 1
    if ex < n and ey < n and not map_list[ey][ex] and not map_list[ey-1][ex] and not map_list[ey][ex-1]:
        if ex == n - 1 and ey == n - 1: cnt += 1
        else: dfs_list.append((2, sx, sy, ex, ey))
    ex -= 1
    if ex < n and ey < n and not map_list[ey][ex]:
        if ex == n - 1 and ey == n - 1: cnt += 1
        else: dfs_list.append((1, sx, sy, ex, ey))

    ex += 1
    ey -= 1
    if ex < n and ey < n and not map_list[ey][ex]:
        if ex == n - 1 and ey == n - 1: cnt += 1
        else: dfs_list.append((0, sx, sy, ex, ey))
    # print('diagonal')
    # print(dfs_list, cnt )
    return cnt


n = int(input().strip())
map_list = list(list(map(int, input().strip().split())) for _ in range(n))

# 방향(가로 0, 세로 1, 대각 2) x1, y1, x2, y2
dfs_list = [(0, 0, 0, 1, 0)]
result_cnt = 0
while dfs_list:
    direc, x1, y1, x2, y2 = dfs_list.pop()
    if not direc: result_cnt += horizontal(x1, y1, x2, y2)
    elif direc == 1: result_cnt += vertical(x1, y1, x2, y2)
    elif direc == 2: result_cnt += diagonal(x1, y1, x2, y2)

print(result_cnt)