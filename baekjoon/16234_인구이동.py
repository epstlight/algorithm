#시뮬레이션


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, l, r = map(int, input().strip().split())
popul_map = list(list(map(int, input().strip().split())) for _ in range(n))
result_cnt = 0
group_list = []
visited = [[0] * n for _ in range(n)]

while True:
    group_num = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                group_num += 1
                visited[y][x] = group_num
                dfs_list = [(x, y)]
                group_sum, group_cnt = popul_map[y][x], 1
                while dfs_list:
                    cx, cy = dfs_list.pop()
                    for i in range(4):
                        xx, yy = cx + dx[i], cy + dy[i]
                        if xx >= 0 and yy >= 0 and xx < n and yy < n and not visited[yy][xx]:
                            if l <= abs(popul_map[cy][cx] - popul_map[yy][xx]) and abs(popul_map[cy][cx] - popul_map[yy][xx]) <= r:
                                visited[yy][xx] = group_num
                                dfs_list.append((xx, yy))
                                group_cnt += 1
                                group_sum += popul_map[yy][xx]
                group_list.append((group_sum, group_cnt))

    if len(group_list) == n*n: break

    for y in range(n):
        for x in range(n):
            if visited[y][x] > 0:
                temp_num, visited[y][x] = visited[y][x], 0
                dfs_list = [(x, y)]
                group_sum, group_cnt = group_list.pop(0)
                temp_popul = group_sum // group_cnt
                popul_map[y][x] = temp_popul

                while dfs_list:
                    cx, cy = dfs_list.pop()
                    for i in range(4):
                        xx, yy = cx + dx[i], cy + dy[i]
                        if xx >= 0 and yy >= 0 and xx < n and yy < n and visited[yy][xx] == temp_num:
                            dfs_list.append((xx, yy))
                            popul_map[yy][xx] = temp_popul
                            visited[yy][xx] = 0
    result_cnt += 1
print(result_cnt)