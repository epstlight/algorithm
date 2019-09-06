#위 오른 아래 왼
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

r, c, t = map(int, input().strip().split())

mise_map = list(list(map(int, input().strip().split())) for _ in range(r))


while t > 0:
    next_mise_map = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if mise_map[y][x] > 0:
                diff_cnt = 0
                for i in range(4):
                    xx, yy = x + dx[i], y + dy[i]
                    if xx >= 0 and yy >= 0 and xx < c and yy < r and mise_map[yy][xx] >= 0:
                        next_mise_map[yy][xx] += mise_map[y][x] // 5
                        diff_cnt += 1
                next_mise_map[y][x] += mise_map[y][x] - (mise_map[y][x] // 5) * diff_cnt
            elif mise_map[y][x] == -1:
                next_mise_map[y][x] = mise_map[y][x]

    # for mise in next_mise_map:
    #     print(mise)
    # print()

    mise_map = [[0] * c for _ in range(r)]
    air_start = 0
    for y in range(r):
        if next_mise_map[y][0] == -1:
            air_start = y
            break

    mise_map[air_start][0] = mise_map[air_start + 1][0] = -1
    for x in range(2, c): mise_map[air_start][x] = next_mise_map[air_start][x - 1]
    for y in range(air_start-1, -1, -1): mise_map[y][c-1] = next_mise_map[y+1][c-1]
    for x in range(c-2, -1, -1): mise_map[0][x] = next_mise_map[0][x+1]
    for y in range(1, air_start): mise_map[y][0] = next_mise_map[y-1][0]

    for y in range(1, air_start):
        for x in range(1, c-1):
            mise_map[y][x] = next_mise_map[y][x]

    air_start += 1
    for x in range(2, c): mise_map[air_start][x] = next_mise_map[air_start][x - 1]
    for y in range(air_start+1, r): mise_map[y][c-1] = next_mise_map[y-1][c-1]
    for x in range(c-2, -1, -1): mise_map[r-1][x] = next_mise_map[r-1][x+1]
    for y in range(r-2, air_start, -1): mise_map[y][0] = next_mise_map[y+1][0]

    for y in range(air_start + 1, r-1):
        for x in range(1, c - 1):
            mise_map[y][x] = next_mise_map[y][x]
    t -= 1

result = 2
for mise in mise_map:
    result += sum(mise)

print(result)

