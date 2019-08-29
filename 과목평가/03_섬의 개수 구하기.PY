

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, -1, 1, 1]

test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n = int(input().strip())
    map_list = list(list(map(int, input().strip().split())) for _ in range(n))
    map_visited = [[False] * n for _ in range(n)]
    result_cnt = 0

    for i in range(n):
        for j in range(n):
            if map_list[i][j] and not map_visited[i][j]:
                dfs_list = [(j, i)]
                map_visited[i][j] = True
                result_cnt += 1

                while dfs_list:
                    x, y = dfs_list.pop()

                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if xx >= 0 and yy >= 0 and xx < n and yy < n and not map_visited[yy][xx] and map_list[yy][xx]:
                            map_visited[yy][xx] = True
                            dfs_list.append((xx, yy))

    print('#%d %d' % (tc, result_cnt))