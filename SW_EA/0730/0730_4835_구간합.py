import sys
sys.stdin = open('input.txt', 'r')

def my_max(a, b):
    return a if a > b else b

def my_min(a, b):
    return a if a < b else b

test_case = int(input())
for tc in range(test_case):
    N, M = map(int, input().strip().split(' '))

    num_list = list(map(int, input().strip().split(' ')))
    max_num = min_num = 0
    for i in range(M): max_num += num_list[i]
    temp_num = min_num = max_num

    for i in range(M, N):
        temp_num = temp_num - num_list[i - M] + num_list[i]
        max_num = my_max(temp_num, max_num)
        min_num = my_min(temp_num, min_num)

    print('#%d %d' %(tc + 1, max_num - min_num))