
def find_result(find_list, find_len):
    cnt = 0
    for i in range(0, 9 - find_len):
        temp_list = find_list[i:find_len + i]
        temp_cnt = 0
        for j in range(find_len // 2):
            if temp_list[j] == temp_list[-(j + 1)]:
                temp_cnt += 1
            else:
                break
        if temp_cnt == (find_len // 2):
            cnt += 1
    return cnt

for tc in range(10):
    map_list = [0] * 8
    find_len = int(input())
    result_cnt = 0

    for i in range(8):
        map_list[i] = list(input().strip()[:])

    for i in range(8):
        temp = []
        for j in range(8):
            temp += map_list[j][i]
        result_cnt += find_result(temp, find_len)
        result_cnt += find_result(map_list[i], find_len)

    print('#%d %d'%(tc + 1, result_cnt))