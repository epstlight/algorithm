#1이면 흑돌, 2이면 백돌

def change_color(color, direc, start_position):
    cx, cy, = start_position
    change_color_list = []
    while True:
        cx, cy = cx + dx[direc], cy + dy[direc]
        if cx < 0 or cy < 0 or cx >= n or cy >= n or bw_map[cy][cx] == 0:
            return
        elif bw_map[cy][cx] == color:
            break
        # elif bw_map[cy][cx] != color:
        else:
            change_color_list.append((cx, cy))
    for cx, cy in change_color_list: bw_map[cy][cx] = color

def cnt_bw(bw_map):
    cnt_list = [0] * 3
    for i in range(n):
        for j in range(n):
            cnt_list[bw_map[i][j]] += 1
    return cnt_list

dx, dy = [1, -1, 0, 0, -1, -1, 1, 1], [0, 0, 1, -1, -1, 1, 1, -1]
for tc in range(1, int(input().strip()) + 1):
    n, m = map(int, input().strip().split())
    bw_map = [[0] * n for _ in range(n)]
    bw_map[n//2 - 1][n//2 - 1] = bw_map[n//2][n//2] = 2
    bw_map[n//2 - 1][n//2] = bw_map[n//2][n//2 - 1] = 1
    for _ in range(m):
        x, y, color = map(int, input().strip().split())
        x, y = x - 1, y - 1
        bw_map[y][x] = color
        for i in range(8):
            xx, yy = x + dx[i], y + dy[i]
            if xx >=0 and yy >= 0 and xx < n and yy < n and bw_map[yy][xx] and bw_map[yy][xx] != color:
                change_color(color, i, (x, y))

        # for a in bw_map:
        #     print(a)
        # print()
    result = cnt_bw(bw_map)
    print('#%d' %tc, result[1], result[2])