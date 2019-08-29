
def find_min_len():
    bfs_list = [(start, 0)]
    node_visited[start] = True

    while bfs_list:
        x, cnt = bfs_list.pop(0)
        for i in range(1, v + 1):
            if node_list[x][i] and not node_visited[i]:
                if i == end:
                    return cnt + 1
                node_visited[i] = True
                bfs_list.append((i, cnt + 1))
    return 0

for tc in range(1, int(input().strip()) + 1):
    v, e = map(int, input().strip().split())
    node_list = [[False] * (v+1) for _ in range(v+1)]
    node_visited = [False] * (v+1)

    for _ in range(e):
        from_, to_ = map(int, input().strip().split())
        node_list[from_][to_] = node_list[to_][from_] = True

    start, end = map(int, input().strip().split())
    print('#%d' %(tc), find_min_len())



