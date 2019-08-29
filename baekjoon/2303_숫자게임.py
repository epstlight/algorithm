'''
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10
output => 1
'''

n = int(input().strip())
nums_list = list(list(map(int, input().strip().split())) for _ in range(n))
max_sum = [0] * n
for k in range(len(nums_list)):
    for i in range(1, 1 << 5):
        select_list = []
        for j in range(5):
            if i & (1 << j):
                select_list.append(nums_list[k][j])
        if len(select_list) == 3:
            max_sum[k] = max(max_sum[k], sum(select_list) % 10)
            if max_sum[k] == 9:
                break

max_sum = list(enumerate(max_sum))
max_sum = sorted(max_sum, key=lambda x:x[1])
print(max_sum[-1][0] + 1)