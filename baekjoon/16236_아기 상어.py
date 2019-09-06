
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

n = int(input().strip())
fish_map = list(list(map(int, input().strip().split())) for _ in range(n))
shark_visited = [[False] * n for _ in range(n)]
shark = (0, 0, 0, 2)
result_time = 0

for i in range(n):
    if 9 in fish_map[i]:
        shark = (fish_map[i].index(9), i, 0, 2)
        fish_map[i][shark[0]] = 0
        shark_visited[i][shark[0]] = True
        break

bfs_list = [shark]
eat_cnt = 0
temp_list = []

while bfs_list:
    x, y, time, size = bfs_list.pop(0)
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx >= 0 and yy >= 0 and xx < n and yy < n and not shark_visited[yy][xx] and size >= fish_map[yy][xx]:
            if size > fish_map[yy][xx] and fish_map[yy][xx] > 0:
                if not temp_list: temp_list.append((yy, xx, time, size))
                else:
                    if temp_list[0][2] < time: break
                    else: temp_list.append((yy, xx, time, size))
                shark_visited[yy][xx] = True
            else:
                shark_visited[yy][xx] = True
                bfs_list.append((xx, yy, time + 1, size))

    if (temp_list and bfs_list and bfs_list[0][2] > temp_list[0][2]) or (temp_list and not bfs_list):
        temp_list.sort()
        # print(temp_list)
        yy, xx, time, size = temp_list[0]

        eat_cnt += 1
        if size == eat_cnt:
            size += 1
            eat_cnt = 0
        shark = (xx, yy, time + 1, size)
        bfs_list = [shark]
        shark_visited = [[False] * n for _ in range(n)]
        shark_visited[yy][xx] = True
        fish_map[yy][xx] = 0
        result_time = time + 1
        temp_list = []

print(result_time)


