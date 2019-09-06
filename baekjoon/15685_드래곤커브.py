# 1 우측 2 위 3 좌측 4 아래
dx, dy = [0, 1, 0, -1, 0], [0, 0, -1, 0, 1]

def rotate_add():
    x, y, direc = dragon_list[-1]
    x += dx[direc]
    y += dy[direc]
    for i in range(len(dragon_list) - 1, -1, -1):
        direc = dragon_list[i][2]
        if direc == 1: direc = 2
        elif direc == 2: direc = 3
        elif direc == 3: direc = 4
        elif direc == 4: direc = 1
        dragon_list.append((x, y, direc))

        if not dragon_map[y][x] or dragon_map[y][x] == True: dragon_map[y][x] = [direc]
        else: dragon_map[y][x].append(direc)

        x += dx[direc]
        y += dy[direc]
        dragon_map[y][x] = True


def check_square(x, y):
    cnt = 0
    for yy in range(y, y + 2):
        for xx in range(x, x + 2):
            if dragon_map[yy][xx]: cnt += 1
    return True if cnt == 4 else False


n = int(input().strip())
dragon_map = [[0] * 101 for _ in range(101)]
result_cnt = 0

for _ in range(n):
    x, y, direc, gene = map(int, input().strip().split())
    dragon_map[y][x] = [direc + 1]
    dragon_map[y + dy[direc+1]][x + dx[direc + 1]] = True
    dragon_list = [(x, y, direc + 1)]
    while gene > 0 :
        rotate_add()
        gene -= 1

for y in range(100):
    for x in range(100):
        if dragon_map[y][x] and check_square(x, y):
            result_cnt += 1

print(result_cnt)
