dx = [1, -1, 0]
dy = [0, 0, 1]

def check_jojak(sadary):
    for a in sadary:
        print(a)
    print()
    visited = [[False] * (2 * n - 1) for _ in range(h)]
    for i in range(0, 2 * n, 2):
        visited[0][i] = True
        x, y = i, 0
        while y < h - 1:
            for j in range(3):
                xx, yy = x + dx[j], y + dy[j]
                if xx >= 0 and yy >= 0 and xx < nn and yy < h and not visited[yy][xx] and sadary_map[yy][xx] == 1:
                    sadary_map[yy][xx] = True
                    x, y = xx, yy
                    break
        if y == h - 1 and x != i: return False
    return True

def sadary_jojak(sadary_map, cnt, current):
    if check_jojak(sadary_map): return cnt
    elif cnt < 3:
        x, y = current
        temp = -1
        for xx in range(x, nn, 2):
            if not sadary_map[y][xx]:
                sadary_map[y][xx] = 1
                temp = max(temp, sadary_jojak(sadary_map, cnt + 1, (xx, y)))
                sadary_map[y][xx] = 0
        for yy in range(y+1, h):
            for xx in range(1, nn, 2):
                if not sadary_map[yy][xx]:
                    sadary_map[yy][xx] = 1
                    temp = max(temp, sadary_jojak(sadary_map, cnt + 1, (xx, yy)))
                    sadary_map[yy][xx] = 0
        return temp
    else: return -1




n, m, h = map(int, input().strip().split())
nn = (2 * n - 1)
sadary_map = [[0] * nn for _ in range(h)]
for y in range(h):
    for i in range(0, nn, 2):
        sadary_map[y][i] = 1

for _ in range(m):
    a, b = map(int, input().strip().split())
    a -= 1
    b = (b - 1) * 2 + 1
    sadary_map[a][b] = 1

print(sadary_jojak(sadary_map, 0, (1, 0)))
# for a in sadary_map:
#     print(a)
# print()
