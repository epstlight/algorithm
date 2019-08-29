
dx = [1, -1, 0]
dy = [0, 0, -1]

for _ in range(10):
    ladder_map = []
    ladder_visited = [[False] * 100 for _ in range(100)]

    tc = int(input())
    for _ in range(100):
        ladder_map.append(list(map(int, input().strip().split())))

    result_bool = False
    ladder_que = []
    result_start = 0
    for i in range(100):
        if ladder_map[99][i] == 2:
            ladder_que.append((i, 99))
            ladder_visited[99][i] = True
            break

    while ladder_que and not result_bool:
        ladder_x, ladder_y = ladder_que.pop()
        for j in range(3):
            xx = ladder_x + dx[j]
            yy = ladder_y + dy[j]
            if xx >= 0 and yy >= 0 and xx < 100 and yy < 100 and ladder_map[yy][xx] == 1 and not ladder_visited[yy][xx]:
                if yy == 0:
                    result_bool = True
                    result_start = xx
                    break
                else:
                    ladder_visited[yy][xx] = True
                    ladder_que.append((xx, yy))
                    break

    print('#%d %d' %(tc, result_start))