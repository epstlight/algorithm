
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input().strip())
map_list = [list(int(char) for char in input()) for _ in range(n)]
map_visited = [[False] * n for _ in range(n)]
dfs_list = []
result_list = []
ground_cnt = 0

for i in range(n):
    for j in range(n):
        if map_list[i][j] and not map_visited[i][j]:
            map_visited[i][j] = True
            dfs_list.append((j, i))
            building_cnt = 1
            ground_cnt += 1
            while dfs_list:
                x, y = dfs_list.pop()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if xx >= 0 and yy >= 0 and xx < n and yy < n and not map_visited[yy][xx] and map_list[yy][xx]:
                        map_visited[yy][xx] = True
                        dfs_list.append((xx, yy))
                        building_cnt += 1
            result_list.append(building_cnt)

result_list.sort()
print(ground_cnt)
for num in result_list:
    print(num)