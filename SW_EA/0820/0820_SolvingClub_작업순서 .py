
for tc in range(1, 11):
    v, e = map(int, input().strip().split())
    map_list = [[False] * (v+1) for _ in range(v+1)]
    map_visited = [False] * (v+1)
    result_list = []
    temp = list(map(int, input().strip().split()))
    for i in range(e):
        map_list[temp[i * 2 + 1]][temp[i * 2]] = True

    while True:
        start_num = 0
        for i in range(1, v + 1):
            if True not in map_list[i] and not map_visited[i]:
                start_num = i
                map_visited[i] = True
                result_list.append(i)
                break
        else:
            break

        dfs_list = [start_num]
        while dfs_list:
            start_num = dfs_list.pop()
            for i in range(1, v + 1):
                if map_list[i][start_num] and not map_visited[i] and not i == start_num:
                    if map_list[i].count(True) == 1:
                        map_visited[i] = True
                        map_list[i][start_num] = False
                        result_list.append(i)
                        dfs_list.append(i)
                        break
            for i in range(1, v + 1):
                map_list[i][start_num] = False
    result = ' '.join(map(str, result_list))
    print('#%d %s' %(tc, result))
    # print(result)


