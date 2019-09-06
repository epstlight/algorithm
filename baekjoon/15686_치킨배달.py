# 0은 빈 칸, 1은 집, 2는 치킨집, bfs문제
import sys, itertools

def min_dist(chichi_list):
    result_dist = 0
    for y in range(n):
        for x in range(n):
            if city_map[y][x] == 1:
                dist = sys.maxsize
                for chicken in chichi_list:
                    dist = min(dist, abs(chicken[0] - x) + abs(chicken[1] - y))
                result_dist += dist
    return result_dist

def select_chicken(num, final_chicken_list, idx):
    dist = sys.maxsize
    if num == m:
        return min_dist(final_chicken_list)
    else:
        for i in range(idx + 1, len(chicken_position) - m + num + 1):
            final_chicken_list.append(chicken_position[i])
            dist = min(dist, select_chicken(num + 1, final_chicken_list, i))
            final_chicken_list.pop()
        return dist

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().strip().split())
city_map = list(list(map(int, input().strip().split())) for _ in range(n))
result = sys.maxsize
chicken_position = []

for y in range(n):
    for x in range(n):
        if city_map[y][x] == 2:
            chicken_position.append((x, y))

if len(chicken_position) > m:
    final_chicken_list = []
    for i in range(len(chicken_position) - m + 1):
        final_chicken_list.append(chicken_position[i])
        result = min(result,  select_chicken(1, final_chicken_list, i))
        final_chicken_list.pop()
else:
    result = min_dist(chicken_position)
print(result)




