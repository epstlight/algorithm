# 상: 0, 하: 1, 좌: 2, 우: 3
from collections import defaultdict

def is_edge(xx, yy):
    if xx >= 1 and yy >= 1 and xx < n-1 and yy < n-1:
        return False
    return True

def solve(m):
    while m > 0:
        m -= 1
        temp_dict = defaultdict(lambda :[])
        for y in range(n):
            for x in range(n):
                if not bugs_dict[(x, y)]: continue
                size, direc = bugs_dict[(x, y)].pop()
                xx, yy = x + dx[direc], y + dy[direc]
                if is_edge(xx, yy):
                    size //= 2
                    if direc == 0 or direc == 2:
                        direc += 1
                    else:
                        direc -= 1
                temp_dict[(xx, yy)].append((size, direc))

        for key, value in temp_dict.items():
            if not value: continue
            x, y = key
            if len(value) > 1:
                value.sort(key=lambda x:x[0], reverse=True)
                direc = value[0][1]
                size = 0
                for s, d in value: size += s
                bugs_dict[(x, y)].append((size, direc))
            else:
                bugs_dict[(x, y)].append((value.pop()))

    result = 0
    for value in bugs_dict.values():
        if value:
            result += value[0][0]
    print('#%d' %tc, result)
    return


dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for tc in range(1, int(input().strip()) + 1):
    n, m, k = map(int, input().strip().split())
    bugs_dict = defaultdict(lambda :[])

    for _ in range(k):
        y, x, size, direc = map(int, input().strip().split())
        direc -= 1
        bugs_dict[(x, y)].append((size, direc))
    solve(m)



