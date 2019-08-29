#dp
'''
5
=> 25
6
=> 42
'''

n = int(input().strip())
dp = [0] * n
if n == 1:
    print(4)
else:
    dp[0] = dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    result = dp[n - 1] * 2 + (dp[n - 1] + dp[n - 2]) * 2
    print(result)
