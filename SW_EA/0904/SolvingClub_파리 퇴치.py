
def cnt_wing(x, y):
    cnt = 0
    for i in range(y, y + m):
        for j in range(x, x + m):
            cnt += wing_map[i][j]
    return cnt


for tc in range(1, int(input().strip()) + 1):
    n, m = map(int, input().strip().split())
    wing_map = list(list(map(int, input().strip().split())) for _ in range(n))
    result_cnt = 0
    for y in range(n-m+1):
        for x in range(n-m+1):
            result_cnt = max(result_cnt, cnt_wing(x, y))
    print('#%d' %tc, result_cnt)