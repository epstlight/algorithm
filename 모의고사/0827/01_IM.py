
def cnt_low_light(paint_list, n, m):
    cnt = [0] * 11
    for i in range(n):
        for j in range(m):
            cnt[paint_list[i][j]] += 1
    return max(cnt)


def check(start_y, start_x, end_y, end_x, light):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if paint_list[y][x] > light:
                return False
    return True


for tc in range(1, int(input().strip()) + 1):
    n, m, k = map(int, input().strip().split())
    paint_list = [[0] * m for _ in range(n)]

    for i in range(k):
        start_y, start_x, end_y, end_x, light = map(int, input().strip().split())
        if check(start_y, start_x, end_y, end_x, light):
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    paint_list[y][x] = light
        else:
            continue

    result_cnt = cnt_low_light(paint_list, n, m)
    print('#%d %d' %(tc, result_cnt))