
def check_xy():
    for garo in sdoku:
        for i in range(1, 10):
            if i not in garo: return False

    for x in range(9):
        temp_sero = []
        for y in range(9):
            temp_sero.append(sdoku[y][x])
        for i in range(1, 10):
            if i not in temp_sero: return False
    return True

def check_sq():
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            temp_sq = []
            for yy in range(y, y + 3):
                temp_sq.extend(sdoku[yy][x:x+3])
            for i in range(1, 10):
                if i not in temp_sq: return False
    return True

for tc in range(1, int(input().strip()) + 1):
    sdoku = list(list(map(int, input().strip().split())) for _ in range(9))

    if check_sq() and check_xy(): print('#%d' %tc, 1)
    else: print('#%d' %tc, 0)
