test_case = int(input())

for tc in range(test_case):
    N, K = map(int, input().strip().split())
    num_list = range(1, 13)
    cnt = 0

    for i in range(1 << 12):
        temp_list = []
        for j in range(12):
            if i & (1 << j):
                temp_list.append(num_list[j])
        if len(temp_list) == N and sum(temp_list) == K:
             cnt += 1

    print('#%d %d' %(tc + 1, cnt))

