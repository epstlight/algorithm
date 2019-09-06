for tc in range(1, int(input().strip())+1):
    n, m = map(int, input().strip().split())
    num_list = []
    for _ in range(m):
        num_list.append(list(map(int, input().strip().split())))

    for i in range(1, m):
        for j in range(len(num_list[0])):
            if num_list[0][j] > num_list[i][0]:
                num_list[0][j:0] = num_list[i]

                break
        else:
            num_list[0].extend(num_list[i])

    print('#%d' %(tc), end=' ')
    for num in num_list[0][-1:-11:-1]:
        print(num, end=' ')
    print()