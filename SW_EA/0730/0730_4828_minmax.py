def my_max(a, b):
    return a if a > b else b

def my_min(a, b):
    return a if a < b else b

tesc_case = int(input())

for tc in range(tesc_case):
    N = int(input())
    num_list = list(map(int, input().strip().split(' ')))
    max_num = min_num = num_list[0]
    for i in range(1, N):
        max_num = my_max(num_list[i], max_num)
        min_num = my_min(num_list[i], min_num)

    print('#%d %d' % (tc+1, max_num - min_num))
