#2 출발 3 도착 1벽

test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n = int(input().strip())
    map_list = [[int(a) for a in input()] for _ in range(n)]
    map_visited = [[False] * n for _ in range(n)]
    result = 0
    bfs_list = []
    for i in range(n):
        for j in range(n):
            if map_list[i][j] == 2:
                bfs_list.append((j, i, 0))
                map_visited[i][j] = True
                break
        if bfs_list: break

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while bfs_list and not result:
        x, y, cnt = bfs_list.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= 0 and yy >= 0 and xx < n and yy < n and map_list[yy][xx] != 1 and not map_visited[yy][xx]:
                if map_list[yy][xx] == 3:
                    result = cnt
                    break
                map_visited[yy][xx] = True
                bfs_list.append((xx, yy, cnt + 1))
        if result: break
    print('#%d %d' %(tc, result))