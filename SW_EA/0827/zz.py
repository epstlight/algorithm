
def min_sum(y, temp_sum):
    global result_min
    if y == n-1:
        for x in range(n):
            if not visited[x]:
                result_min = min(result_min, result_min, map_list[y][x] + temp_sum)
    else:
        for x in range(n):
            if not visited[x] and result_min > temp_sum + map_list[y][x]:
                visited[x] = True
                result_min = min(result_min, min_sum(y + 1, temp_sum + map_list[y][x]))
                visited[x] = False
    return result_min



for tc in range(1, int(input().strip())+1):
    n = int(input().strip())
    map_list = list(list(map(int, input().strip().split())) for _ in range(n))
    visited = [False] * n
    result_min = 10000
    min_sum(0, 0)
    print('#%d' %(tc), result_min)
