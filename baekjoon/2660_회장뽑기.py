
def dfs(i):
    dfs_list = [(i, 0)]
    dfs_visited = [False] * (n + 1)
    dfs_visited[0] = dfs_visited[i] = True
    final_score = 0
    while dfs_list and False in dfs_visited:
        # dfs말고 bfs 써야댐 가장 빨라야되서
        num, score = dfs_list.pop(0)
        for j in range(1, n + 1):
            if map_list[num][j] and not dfs_visited[j]:
                dfs_visited[j] = True
                dfs_list.append((j, score + 1))
                final_score = score + 1
    return final_score



n = int(input().strip())
map_list = [[False] * (n+1) for _ in range(n+1)]

while True:
    temp_a, temp_b = map(int, input().strip().split())
    if temp_a == -1 and temp_b == -1:
        break
    map_list[temp_a][temp_b] = map_list[temp_b][temp_a] = True

result_list = [0] * (n + 1)
for i in range(1, n + 1):
    result_list[i] = dfs(i)

min = 10000
min_list = []
for i in range(1, n+1):
    if result_list[i] > 0 and min > result_list[i]:
        min = result_list[i]
        min_list = [i]
    elif min == result_list[i]:
        min_list.append(i)

min_list.sort()
print(min, len(min_list), sep=' ')
for num in min_list:
    print(num, end=' ')
