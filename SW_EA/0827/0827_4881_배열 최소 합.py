import sys

def find_min_sum(y, min_sum):
    global result_min
    for i in range(n):
        if not select_limit[i]:
            if y < n - 1 and result_min > map_list[y][i] + min_sum:
                select_limit[i] = True
                result_min = min(result_min, find_min_sum(y + 1, map_list[y][i] + min_sum))
                select_limit[i] = False
            else:
                result_min = min(result_min, min_sum + map_list[y][i])
    return result_min


for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    map_list = list(list(map(int, input().strip().split())) for _ in range(n))
    select_limit = [False] * n
    result_min = sys.maxsize
    print('#%d %d' %(tc, find_min_sum(0, 0)))



