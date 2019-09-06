

dx = [0, 1]
dy = [1, 0]

def cnt_blank(x, y, direc):
    cnt = 0
    while x < n and y < n and puzzle_map[y][x] == 1:
        cnt += 1
        x += dx[direc]
        y += dy[direc]
    return True if cnt == k else False


for tc in range(1, int(input().strip()) + 1):
    n, k = map(int, input().strip().split())

    puzzle_map = list(list(map(int, input().strip().split())) for _ in range(n))
    result_cnt = 0

    for y in range(n):
        for x in range(n):
            if puzzle_map[y][x]:
                if x - 1 < 0 or (x - 1 >= 0 and not puzzle_map[y][x-1]):
                    if cnt_blank(x, y, 1): result_cnt += 1
                if y - 1 < 0 or (y - 1 >= 0 and not puzzle_map[y-1][x]):
                    if cnt_blank(x, y, 0): result_cnt += 1

    print('#%d' %tc, result_cnt)