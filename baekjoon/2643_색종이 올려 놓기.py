
n = int(input().strip())
paper_list = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().strip().split())
    paper_list.append((min(a, b), max(a, b), a*b))
    # paper_list[1].append(max(a, b))
    # paper_list[2].append(a*b)

# for i in range(n):
#     for j in range(i + 1, n):
#         if paper_list[2][i] > paper_list[2][j]:
#             paper_list[0][i], paper_list[0][j] = paper_list[0][j], paper_list[0][i]
#             paper_list[1][i], paper_list[1][j] = paper_list[1][j], paper_list[1][i]
#             paper_list[2][i], paper_list[2][j] = paper_list[2][j], paper_list[2][i]

paper_list = sorted(paper_list, key=lambda x:x[2])
for i in range(n):
    for j in range(i - 1, -1, -1):
        if paper_list[j][0] <= paper_list[i][0] and paper_list[j][1] <= paper_list[i][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
