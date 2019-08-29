testcase = int(input())

for tc in range(testcase):
    n = int(input())
    temp = list(map(int, input().strip().split()))
    front_bolts = temp[0::2]
    back_bolts = temp[1::2]
    result_list = []
    idx = 0

    for i in range(n):
        if front_bolts[i] not in back_bolts:
            idx = i

    for _ in range(n):
        result_list.append(str(front_bolts[idx]))
        result_list.append(str(back_bolts[idx]))
        for i in range(n):
            if back_bolts[idx] == front_bolts[i]:
                idx = i
                break

    print('#{} {}'.format(tc + 1, ' '.join(result_list)))

