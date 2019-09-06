import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(k):
    global tree_cnt
    while k > 0:
        # 봄, 여름
        k -= 1
        for x in range(n):
            for y in range(n):
                if not tree_dict[(x, y)]:
                    if k > 0: current_food[x][y] += winter_add_food[x][y]
                    continue

                readd_tree = []
                while tree_dict[(x, y)]:
                    age = tree_dict[(x, y)].pop()
                    if age > current_food[x][y]:
                        current_food[x][y] += (age // 2)
                        tree_cnt -= 1
                        while tree_dict[(x, y)]:
                            age = tree_dict[(x, y)].pop()
                            current_food[x][y] += (age // 2)
                            tree_cnt -= 1
                    else:
                        current_food[x][y] -= age
                        readd_tree.append(age + 1)
                # 여름
                if readd_tree:
                    tree_dict[(x, y)].extend(readd_tree[::-1])
                if k > 0: current_food[x][y] += winter_add_food[x][y]

        for key, value in tree_dict.items():
            if not value: continue
            cnt = 0
            for age in value:
                if age < 5: break
                if age % 5 == 0:
                    cnt += 1
            if cnt:
                x, y = key
                for i in range(8):
                    xx, yy = x + dx[i], y + dy[i]
                    if xx >= 0 and yy >= 0 and xx < n and yy < n:
                        tree_dict[(xx, yy)].extend([1] * cnt)
                        tree_cnt += cnt
    return tree_cnt

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().strip().split())
winter_add_food = list(list(map(int, input().strip().split())) for _ in range(n))
current_food = [[5] * n for _ in range(n)]
tree_dict = defaultdict(lambda:[])
tree_cnt = 0
# 나무 추가 및 정렬
for _ in range(m):
    x, y, age = map(int, input().strip().split())
    tree_dict[(x-1, y-1)].append(age)
    tree_cnt += 1
print(solve(k))

'''
10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1
=> 5443
'''