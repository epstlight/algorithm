
def cnt_black(map_list, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if map_list[i][j]:
                cnt += 1
    return cnt


test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n, m = map(int, input().strip().split())
    map_list = [[False] * n for _ in range(n)]

    for _ in range(m):
        start_y, start_x, end_y, end_x = map(int, input().strip().split())
        for y in range(start_y - 1, end_y):
            for x in range(start_x - 1, end_x):
                if not map_list[y][x]:
                    map_list[y][x] = True

    result_cnt = cnt_black(map_list, n)
    print('#%d %d' %(tc, result_cnt))
