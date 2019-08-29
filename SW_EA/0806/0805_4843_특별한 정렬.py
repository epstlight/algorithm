test_case = int(input())

for tc in range(test_case):
    N = int(input())
    num_list = list(map(int, input().strip().split(' ')))
    result_list = [0] * 10

    for i in range(N):
        for j in range(1, N - i):
            if num_list[j - 1] > num_list[j]:
                num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]

    for i in range(5):
        result_list[2 * i] = num_list[-(i + 1)]
        result_list[2 * i + 1] = num_list[i]

    print('#%d' %(tc + 1),end=' ')
    for result in result_list:
        print(result, end=' ')
    print()
