
def sq_sum(num_list, x, y, k):
    sum_num = 0
    for i in range(x, x + k):
        sum_num += num_list[y][i]
        sum_num += num_list[y + k - 1][i]
    for i in range(y + 1, y + k - 1):
        sum_num += num_list[i][x]
        sum_num += num_list[i][x + k - 1]
    return sum_num


test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n, m, k = map(int, input().strip().split())
    num_list = list(list(map(int, input().strip().split())) for _ in range(n))
    max_sum = 0
    for y in range(n - k + 1):
        for x in range(m - k + 1):
            max_sum = max(max_sum, sq_sum(num_list, x, y, k))

    print('#%d %d' %(tc, max_sum))
