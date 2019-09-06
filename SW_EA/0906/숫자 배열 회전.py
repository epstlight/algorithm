import copy

def rotate():
    temp_list = copy.deepcopy(num_map)
    for y in range(n):
        for x in range(n):
            num_map[x][(n-1) - y] = temp_list[y][x]

for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    num_map = list(input().strip().split() for _ in range(n))
    result_list = [[] for _ in range(n)]
    for _ in range(3):
        rotate()
        for i in range(n):
            result_list[i].append(''.join(num_map[i]))

    print('#%d' %tc)
    for nums in result_list:
        print(' '.join(nums))
