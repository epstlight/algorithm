test_case = int(input())

for tc in range(test_case):
    xy_map = [[0] * 10 for _ in range(10)]
    N = int(input())
    pp_cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().strip().split(' '))
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if xy_map[r][c] == 0: xy_map[r][c] += color
                elif xy_map[r][c] == 1 and color == 2:
                    xy_map[r][c] += color
                    pp_cnt += 1
                elif xy_map[r][c] == 2 and color == 1:
                    xy_map[r][c] += color
                    pp_cnt += 1

    print('#%d %d' %(tc + 1, pp_cnt))
