
def solve(data):
    n = data[0]
    start_num = data[1]
    from_to_list = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(0, len(data[2]), 2):
        from_to_list[data[2][i]][data[2][i + 1]] = True
    return bfs(start_num, from_to_list, n)

def bfs(num, from_to_list, n):
    visited = [False] * (n + 1)
    bfs_list = [(num, 1)]
    visited[num] = True
    max_cnt = 1
    max_num = num
    while bfs_list:
        x, cnt = bfs_list.pop(0)
        for to in range(1, n + 1):
            if from_to_list[x][to] and not visited[to]:
                visited[to] = True
                bfs_list.append((to, cnt + 1))
                if cnt + 1 > max_cnt:
                    max_cnt = cnt + 1
                    max_num = to
                elif cnt + 1 == max_cnt:
                    max_num = max(max_num, to)
    return max_num

input_data = [[0, 0, None] for _ in range(10)]
for i in range(10):
    n, start = map(int, input().strip().split())
    input_data[i][0] = n
    input_data[i][1] = start
    input_data[i][2] = list(map(int, input().strip().split()))

for tc_num, tc_data in enumerate(input_data):
    print('#%d' %(tc_num + 1), solve(tc_data))

