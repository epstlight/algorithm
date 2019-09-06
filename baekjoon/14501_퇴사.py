#dp
n = int(input().strip())
consult_list = [[0, 0] for _ in range(n+1)]
dp = [0] * (n+1)
for i in range(1, n+1): consult_list[i][0], consult_list[i][1] = map(int, input().strip().split())


for i in range(1, n+1):
    if i + consult_list[i][0] > n + 1:
        dp[i] = max(dp[:i])
    else:
        dp[i] = consult_list[i][1]
        temp_max = 0
        for j in range(i-1, -1, -1):
            if consult_list[j][0] <= i-j:
                temp_max = max(temp_max, dp[j])
        dp[i] += temp_max

print(max(dp))
