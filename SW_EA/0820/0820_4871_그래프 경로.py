
test_case = int(input())
for tc in range(1, test_case + 1):
    v, e = map(int, input().strip().split())
    map_list = [[] for _ in range(v+1)]
    result = 0
    for _ in range(e):
        i, j = map(int, input().strip().split())
        map_list[i].append(j)

    start, end = map(int, input().strip().split())
    dfs_list = [start]
    while dfs_list:
        step = dfs_list.pop()
        if map_list[step]:
            if end in map_list[step]:
                result = 1
                break
            dfs_list.extend(map_list[step])
    print('#%d %d' % (tc, result))