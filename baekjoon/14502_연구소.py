#0은 빈 칸, 1은 벽, 2는 바이러스
import copy

def cnt_safe(ground):
    visited = [[False] * m for _ in range(n)]
    virus_map = copy.deepcopy(ground)
    safy_groud = 0
    for y in range(n):
        for x in range(m):
            if virus_map[y][x] == 2 and not visited[y][x]:
                visited[y][x] = True
                dfs_list = [(x, y)]

                while dfs_list:
                    cx, cy = dfs_list.pop()
                    for i in range(4):
                        xx, yy = cx + dx[i], cy + dy[i]
                        if xx >= 0 and yy >= 0 and xx < m and yy < n and not visited[yy][xx] and not virus_map[yy][xx]:
                            visited[yy][xx] = True
                            virus_map[yy][xx] = 2
                            dfs_list.append((xx, yy))
    for y in range(n):
        for x in range(m):
            if not virus_map[y][x]: safy_groud += 1
    return safy_groud


def select_safe_groud(current, num, ground_map):
    max_num = 0
    if num == 3:
        return cnt_safe(ground_map)
    else:
        for x in range(current[0], m):
            if ground_map[current[1]][x] == 0:
                ground_map[current[1]][x] = 1
                max_num = max(max_num, select_safe_groud((x + 1, current[1]), num + 1, ground_map))
                ground_map[current[1]][x] = 0
        for y in range(current[1] + 1, n):
            for x in range(m):
                if ground_map[y][x] == 0:
                    ground_map[y][x] = 1
                    max_num = max(max_num, select_safe_groud((x + 1, y), num + 1, ground_map))
                    ground_map[y][x] = 0
        return max_num


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
n, m = map(int, input().strip().split())
ground_map = list(list(map(int, input().strip().split())) for _ in range(n))
result = select_safe_groud((0, 0), 0, ground_map)
print(result)