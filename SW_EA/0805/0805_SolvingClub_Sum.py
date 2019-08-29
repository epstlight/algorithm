def my_max(a, b):
    return a if a > b else b

def row_column_sum(xy_map, xy):
    result_sum1 = result_sum2 = 0
    for i in range(100):
        result_sum1 += xy_map[xy][i]
        result_sum2 += xy_map[i][xy]
    return my_max(result_sum1, result_sum2)

for _ in range(10):
    tc_num = int(input())
    max_result_num = 0
    xy_map = [0] * 100
    cross_sum1 = cross_sum2 = 0
    for i in range(100):
        xy_map[i] = list(map(int, input().strip().split(' ')))
    for i in range(100):
        max_result_num = my_max(max_result_num, row_column_sum(xy_map, i))
        cross_sum1 += xy_map[i][i]
        cross_sum2 += xy_map[99 - i][i]
    print('#%d %d' %(tc_num, my_max(my_max(max_result_num, cross_sum1), cross_sum2)))

