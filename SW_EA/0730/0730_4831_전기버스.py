
test_case = int(input())

for tc in range(test_case):
    K, N, M = map(int, input().strip().split(' '))
    charge_cnt = 0
    charge_station = list(map(int, input().strip().split(' ')))

    my_location = 0
    while my_location <= N:
        for i in range(my_location + K, my_location, -1):
            if i >= N:
                my_location = i
                break
            elif i in charge_station:
                my_location = i
                charge_cnt += 1
                break
        else:
            charge_cnt = 0

        if charge_cnt == 0:
            break

    print('#%d %d' % (tc + 1, charge_cnt))
