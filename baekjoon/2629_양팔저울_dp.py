
n = int(input().strip())
n_list = list(map(int, input().strip().split()))
find_ball_num = int(input().strip())
find_ball_list = list(map(int, input().strip().split()))
result = ['N'] * find_ball_num
dp = [False] * 40001
visit_list = []
dp[0] = True
for num in n_list:
    dp[num] = True
    visit_list.append(num)

    for i in visit_list[:-1]:
        temp = num + i
        if not dp[temp]:
            dp[temp] = True
            visit_list.append(temp)

        temp = abs(i - num)
        if not dp[temp]:
            dp[temp] = True
            visit_list.append(temp)

for find_ball in find_ball_list:
    if dp[find_ball]:
        print('Y', end=' ')
    else:
        print('N', end=' ')

