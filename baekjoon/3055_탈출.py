#  비어있는곳 . 0,  물 * 1, 돌 X 2 굴 D 3, 고슴도치 S 4
'''
3 3
D.*
...
.S.
=> 3
'''

def simul(gosm_locations, water_locations):
    time = 0
    while gosm_locations:
        next_water_locations = []
        for x, y in water_locations:
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if xx >= 0 and yy >= 0 and xx < c and yy < r and not map_visited[yy][xx] and not map_list[yy][xx]:
                    next_water_locations.append((xx, yy))
                    map_visited[yy][xx] = True
                    map_list[yy][xx] = 1

        water_locations = next_water_locations[:]
        next_gosm_locations = []
        for x, y in gosm_locations:
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if xx >= 0 and yy >= 0 and xx < c and yy < r and not gosm_visited[yy][xx]:
                    if map_list[yy][xx] == 3:
                        time += 1
                        return time
                    elif map_list[yy][xx] == 0 :
                        gosm_visited[yy][xx] = True
                        next_gosm_locations.append((xx, yy))

        gosm_locations = next_gosm_locations[:]
        time += 1
    return 'KAKTUS'


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c = map(int, input().strip().split())
map_list = [[] for _ in range(r)]
gosm_locations = []
water_locations = []
map_visited = [[False] * c for _ in range(r)]
gosm_visited = [[False] * c for _ in range(r)]

for i in range(r):
    temp = input()
    for j in range(len(temp)):
        if temp[j] == '.':
            map_list[i].append(0)
        elif temp[j] == '*': #물이 이동할 수 있는 곳은 0
            map_list[i].append(1)
            water_locations.append((j, i))
            map_visited[i][j] = True

        elif temp[j] == 'X':
            map_list[i].append(2)
        elif temp[j] == 'D':
            map_list[i].append(3)
        else:
            map_list[i].append(0)
            gosm_visited[i][j] = True
            gosm_locations.append((j, i))
print(simul(gosm_locations, water_locations))





