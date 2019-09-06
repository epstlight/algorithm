T = int(input().strip())
input_data = []
for _ in range(T):
    n = int(input().strip())
    input_data.append(list(list(map(int, input().strip().split())) for _ in range(n)))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve(data):
    n = len(data)
    visited = [[False] * n for _ in range(n)]
    result_list = []
    for y in range(n):
        for x in range(n):
            if data[y][x] and not visited[y][x]:
                bfs_list = [(x, y)]
                visited[y][x] = True
                start_x, start_y = end_x, end_y = x, y

                while bfs_list:
                    cx, cy = bfs_list.pop(0)
                    for i in range(4):
                        xx, yy = cx + dx[i], cy + dy[i]
                        if xx >= 0 and yy >= 0 and xx < n and yy < n and data[yy][xx] and not visited[yy][xx]:
                            visited[yy][xx] = True
                            end_x = max(end_x, xx)
                            end_y = max(end_y, yy)
                            bfs_list.append((xx, yy))
                temp_x, temp_y = end_x - start_x + 1, end_y - start_y + 1
                result_list.append((temp_x * temp_y, temp_y, temp_x))

    result_list.sort()
    result_str = str(len(result_list)) + ' '
    for xy, y, x in result_list:
        result_str += str(y) + ' ' + str(x) + ' '
    return result_str

for tc, case in enumerate(input_data):
    print('#%s' %(tc + 1), solve(case))