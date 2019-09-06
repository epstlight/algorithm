
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    n_map = list(list(int(a) for a in input().strip()) for _ in range(n))
    result_sum = 0

    if n == 1: result_sum = n_map[0][0]
    else:
        mid = n // 2
        k = -1
        for y in range(n):
            k = (k - 1) if y > mid else (k + 1)
            for x in range(mid - k, mid + k + 1):
                result_sum += n_map[y][x]

    print('#%d' %tc, result_sum)