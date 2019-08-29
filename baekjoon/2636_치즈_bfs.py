
def check_island():
    bfs_list = []
    cheeze_visited[0][nx-1] = True
    bfs_list.append((nx-1, 0))
    cheeze_visited[ny-1][0] = True
    bfs_list.append((0, ny-1))
    cheeze_visited[0][0] = True
    bfs_list.append((0, 0))
    cheeze_visited[ny-1][nx-1] = True
    bfs_list.append((nx-1, ny-1))
    while bfs_list:
        x, y = bfs_list.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx >= 0 and yy >= 0 and xx < nx and yy < ny and not cheeze_visited[yy][xx] and not cheeze_map[yy][xx]:
                cheeze_visited[yy][xx] = True
                bfs_list.append((xx, yy))


def remain_cheeze(cheeze_map):
    cheeze_num = 0
    for i in range(ny):
        for j in range(nx):
            if cheeze_map[i][j]:
                cheeze_num += 1
    return cheeze_num


def melting():
    for i in range(ny):
        for j in range(nx):
            if melting_cheeze[i][j]:
                cheeze_map[i][j] = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ny, nx = map(int, input().strip().split())
cheeze_map = list(list(map(int, input().strip().split())) for _ in range(ny))
day = 0
remain_cheeze_num = 0
while remain_cheeze(cheeze_map):
    cheeze_visited = [[False] * nx for _ in range(ny)]
    melting_cheeze = [[False] * nx for _ in range(ny)]
    check_island()
    day += 1
    remain_cheeze_num = remain_cheeze(cheeze_map)

    for i in range(ny):
        for j in range(nx):
            if cheeze_map[i][j] and not cheeze_visited[i][j]:
                cheeze_bfs = [(j, i)]
                while cheeze_bfs:
                    x, y = cheeze_bfs.pop(0)
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if xx >= 1 and yy >= 1 and xx < nx-1 and yy < ny-1 and not cheeze_visited[yy][xx] and cheeze_map[yy][xx]:
                            cheeze_visited[yy][xx] = True
                            cheeze_bfs.append((xx, yy))
                        elif cheeze_visited[yy][xx] and not cheeze_map[yy][xx]:
                            melting_cheeze[y][x] = True
    melting()
print(day)
print(remain_cheeze_num)
