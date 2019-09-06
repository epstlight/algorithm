

for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    num_list = [[1] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, i + 1):
            if i == j :
                num_list[i].append(1)
            else:
                num_list[i].append(num_list[i-1][j] + num_list[i-1][j-1])
    print('#%d' %tc)
    for a in num_list:
        for b in a:
            print(b, end=' ')
        print()
