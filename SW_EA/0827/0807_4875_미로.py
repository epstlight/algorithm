#2 출발 3 도착 1벽

test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n = int(input().strip())
    map_list = [[] for _ in range(n)]
    map_visited = [[False] * n for _ in range(n)]

    bfs_list = []
    result = 0
    for i in range(n):
        temp = input().strip()
        for j in range(len(temp)):
            map_list[i].append(int(temp[j]))
            if map_list[i][j] == 2:
                bfs_list.append((j, i))
                map_visited[i][j] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while bfs_list and not result:
        x, y = bfs_list.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx >= 0 and yy >= 0 and xx < n and yy < n and map_list[yy][xx] != 1 and not map_visited[yy][xx]:
                if map_list[yy][xx] == 3:
                    result = 1
                    break
                map_visited[yy][xx] = True
                bfs_list.append((xx, yy))

    print('#%d %d' %(tc, result))

'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''