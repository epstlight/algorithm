'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
output => 2
'''
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().strip().split())
bing_map = list(list(map(int, input().strip().split())) for _ in range(n))
year = 0
bing_cnt = 1
while bing_cnt == 1:
    bing_cnt = 0
    bing_visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if bing_map[i][j] and not bing_visited[i][j]:
                dfs_list = [(j, i)]
                bing_visited[i][j] = True
                bing_cnt += 1
                if bing_cnt > 1:
                    break
                while dfs_list:
                    x, y = dfs_list.pop()
                    zero_cnt = 0
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if xx >= 0 and yy >= 0 and xx < m and yy < n and not bing_visited[yy][xx]:
                            if not bing_map[yy][xx]: zero_cnt += 1
                            else:
                                bing_visited[yy][xx] = True
                                dfs_list.append((xx, yy))
                    if bing_map[y][x] <= zero_cnt:
                        bing_map[y][x] = 0
                    else: bing_map[y][x] -= zero_cnt
        if bing_cnt > 1:
            break
    # for a in bing_map:
    #     print(a)
    # print()
    year += 1

if bing_cnt > 1: print(year - 1)
else: print(0)


