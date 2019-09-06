# up 0 down 1 left 2 right 3

for tc in range(1, int(input().strip()) + 1):
    n, direc = input().strip().split()
    n = int(n)
    direc = 0 if direc == 'up' else 1 if direc == 'down' else 2 if direc == 'left' else 3
    num_map = list(list(map(int, input().strip().split())) for _ in range(n))
    plus_visited = [[False] * n for _ in range(n)]

    if not direc:
        for y in range(1, n):
            for x in range(n):
                if num_map[y][x]:
                    for yy in range(y, 0, -1):
                        if not num_map[yy-1][x]:
                            num_map[yy-1][x], num_map[yy][x] = num_map[yy][x], num_map[yy-1][x]
                        elif num_map[yy-1][x] == num_map[yy][x] and not plus_visited[yy-1][x] and not plus_visited[yy][x]:
                            num_map[yy - 1][x] *= 2
                            num_map[yy][x] = 0
                            plus_visited[yy-1][x] = True
                        else: break

    elif direc == 1:
        for y in range(n - 2, -1, -1):
            for x in range(n):
                if num_map[y][x]:
                    for yy in range(y, n-1):
                        if not num_map[yy+1][x]:
                            num_map[yy+1][x], num_map[yy][x] = num_map[yy][x], num_map[yy+1][x]

                        elif num_map[yy + 1][x] == num_map[yy][x] and not plus_visited[yy+1][x] and not plus_visited[yy][x]:
                            num_map[yy+1][x] *= 2
                            num_map[yy][x] = 0
                            plus_visited[yy+1][x] = True
                        else: break

    elif direc == 2:
        for x in range(1, n):
            for y in range(n):
                if num_map[y][x]:
                    for xx in range(x, 0, -1):
                        if not num_map[y][xx - 1]:
                            num_map[y][xx - 1], num_map[y][xx] = num_map[y][xx], num_map[y][xx - 1]

                        elif num_map[y][xx - 1] == num_map[y][xx] and not plus_visited[y][xx - 1] and not plus_visited[y][xx]:
                            num_map[y][xx - 1] *= 2
                            num_map[y][xx] = 0
                            plus_visited[y][xx - 1] = True
                        else: break
    elif direc == 3:
        for x in range(n - 2, -1, -1):
            for y in range(n):
                if num_map[y][x]:
                    for xx in range(x, n-1):
                        if not num_map[y][xx + 1]:
                            num_map[y][xx + 1], num_map[y][xx] = num_map[y][xx], num_map[y][xx + 1]

                        elif num_map[y][xx + 1] == num_map[y][xx] and not plus_visited[y][xx + 1] and not plus_visited[y][xx]:
                            num_map[y][xx + 1] *= 2
                            num_map[y][xx] = 0
                            plus_visited[y][xx + 1] = True
                        else: break

    print('#%d' %tc)
    for a in num_map:
        for b in a:
            print(b, end=' ')
        print()