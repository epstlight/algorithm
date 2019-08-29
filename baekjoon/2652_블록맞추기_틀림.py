
def check_map_zero():
    start_zero_x = start_zero_y = end_zero_x = end_zero_y = 0
    start_bool = False

    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            if not map_list[i][j]:

                if not start_bool:
                    start_zero_x, start_zero_y = end_zero_x, end_zero_y =j, i
                    start_bool = True
                else: end_zero_x, end_zero_y = j, i
    return start_zero_x, start_zero_y, end_zero_x, end_zero_y

def calc(u, v, w, x, y):
    # 구멍이 오른쪽
    if end_x == end_zero_x:
        u1 = end_y - start_y + 1
        w1 = end_y - end_zero_y
        x1 = end_zero_x - start_zero_x + 1
        y1 = end_zero_y - start_zero_y + 1
        temp_x = end_x + v

        if u1 == u and w1 == w and x1 == x and y1 == y and temp_x < n:
            for i in range(start_y, end_y + 1):
                for j in range(end_x + 1, temp_x + 1):
                    if map_list[i][j]: return False
            return True
        else: return False

    # 구멍이 아래쪽
    elif end_zero_y == end_y:
        u1 = end_x - start_x + 1
        w1 = start_zero_x - start_x
        x1 = end_zero_y - start_zero_y + 1
        y1 = end_zero_x - start_zero_x + 1
        temp_y = end_y + v

        if u1 == u and w1 == w and x1 == x and y1 == y and temp_y < n:
            for i in range(start_x, end_x + 1):
                for j in range(end_y + 1, temp_y + 1):
                    if map_list[j][i]: return False
            return True
        else: return False

    # 구멍이 왼쪽
    elif start_x == start_zero_x:
        u1 = end_y - start_y + 1
        w1 = start_zero_y - start_y
        x1 = end_zero_x - start_zero_x + 1
        y1 = end_zero_y - start_zero_y + 1
        temp_x = start_x - v

        if u1 == u and w1 == w and x1 == x and y1 == y and temp_x >= 0:
            for i in range(start_y, end_y + 1):
                for j in range(temp_x, start_x):
                    if map_list[i][j]: return False
            return True
        else: return False

    # 구멍이 위쪽
    else:
        u1 = end_x - start_x + 1
        w1 = end_x - end_zero_x
        x1 = end_zero_y - start_zero_y + 1
        y1 = end_zero_x - start_zero_x + 1
        temp_y = start_y - v

        if u1 == u and w1 == w and x1 == x and y1 == y and temp_y >= 0:
            for i in range(start_x, end_x + 1):
                for j in range(temp_y, start_y):
                    if map_list[j][i]: return False
            return True
        else: return False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input().strip())
u, v, w, x, y = map(int, input().strip().split())
map_list = list(list(map(int, input().strip().split())) for _ in range(n))
map_visited = [[False] * n for _ in range(n)]
result_list = []

for i in range(n):
    for j in range(n):
        if map_list[i][j] and not map_visited[i][j]:
            start_x, start_y = end_x, end_y = j, i
            map_visited[i][j] = True
            bfs_list = [(j, i)]

            while bfs_list:
                origin_x, origin_y = bfs_list.pop(0)

                for k in range(4):
                    xx, yy = origin_x + dx[k], origin_y + dy[k]

                    if xx >= start_x and yy >= start_y and xx < n and yy < n and map_list[yy][xx] and not map_visited[yy][xx]:
                        map_visited[yy][xx] = True
                        end_x, end_y = max(end_x, xx), max(end_y, yy)
                        bfs_list.append((xx, yy))

            start_zero_x, start_zero_y, end_zero_x, end_zero_y = check_map_zero()

            if calc(u, v, w, x, y):
                result_list.append((start_y + 1, start_x + 1))

if not result_list:
    print(0)
    print()
else:
    print(len(result_list))
    while result_list:
        result_y, result_x = result_list.pop(0)
        print(result_y, result_x)
