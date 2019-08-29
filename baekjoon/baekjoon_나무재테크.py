dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

N, plant_tree, years = map(int, input().split(' '))
src_map = [0] * N
tree_set = set()
next_tree_set = set()
tree_map = [[[5, []] for _ in range(N)] for _ in range(N)]
for i in range(N):
    src_map[i] = list(map(int, input().split(' ')))

for _ in range(plant_tree):
    r, c, age = map(int, input().split(' '))
    tree_map[r-1][c-1][1].append(age)
    if (r-1, c-1) not in tree_set:
        tree_set.add((r - 1, c - 1))

for year in range(years):
    while tree_set:
        r, c = tree_set.pop()
        temp_energy = 0
        temp_list = []
        tree_map[r][c][1].sort()
        # 봄
        for age in tree_map[r][c][1]:
            if tree_map[r][c][0] < age:
                temp_energy += age // 2
            else:
                tree_map[r][c][0] -= age
                temp_list.append(age + 1)
                if (r, c) not in next_tree_set:
                    next_tree_set.add((r, c))
        #여름
        tree_map[r][c][0] += temp_energy
        tree_map[r][c][1] = temp_list[:]
     #가을
    while next_tree_set:
        r, c = next_tree_set.pop()
        tree_set.add((r, c))
        for i in tree_map[r][c][1]:
            if not i % 5:
                for j in range(8):
                    rr = r + dy[j]
                    cc = c + dx[j]
                    if rr >= 0 and cc >= 0 and rr < N and cc < N:
                        tree_set.add((rr, cc))
                        tree_map[rr][cc][1].append(1)

    if year == years - 1:
        break
     #겨울
    for i in range(N):
        for j in range(N):
            tree_map[i][j][0] += src_map[i][j]

tree_num = 0
for r, c in tree_set:
    tree_num += len(tree_map[r][c][1])
print(tree_num)