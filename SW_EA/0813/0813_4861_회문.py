
def find_result(find_list, find_len, N):
    for i in range(0, N + 1 - find_len):
        temp_list = find_list[i:find_len + i]
        temp_cnt = 0
        for j in range(find_len // 2):
            if temp_list[j] == temp_list[-(j + 1)]:
                temp_cnt += 1
            else:
                break
        if temp_cnt == (find_len // 2):
            return temp_list

    return False

testcase = int(input())

for tc in range(testcase):
    N, M = map(int, input().split())
    map_list = [0] * N
    result_str = ''
    for i in range(N):
        map_list[i] = list(input().strip()[:])

    for i in range(N):
        temp = []
        for j in range(N):
            temp += map_list[j][i]

        result_str = find_result(temp, M, N)
        if result_str: break
        result_str = find_result(map_list[i], M, N)
        if result_str: break
    print('#%d %s'%(tc + 1, ''.join(result_str)))
