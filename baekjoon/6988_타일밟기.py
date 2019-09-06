#dp
n = int(input().strip())
n_list = list(map(int, input().strip().split()))
dp = [0] * n
visited = [False] * (n_list[-1] + 1)

for num in n_list: visited[num] = True

for start in range(len(n_list)-2):
    max_num = 0
    for j in range(start + 1, len(n_list)-1):
        i = n_list[j] - n_list[start]
        current = n_list[start] + i
        temp_num = n_list[start]
        cnt = 1
        while current <= n_list[-1] and visited[current]:
            temp_num += current
            current += i
            cnt += 1
        if cnt > 2: max_num = max(max_num, temp_num)
    dp[start] = max_num

print(max(dp))


