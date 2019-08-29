
def find_result(find_list, find_len):
    for i in range(0, 101 - find_len):
        temp_list = find_list[i:find_len + i]
        temp_cnt = 0
        for j in range(find_len // 2):
            if temp_list[j] == temp_list[-(j + 1)]:
                temp_cnt += 1
            else:
                break
        if temp_cnt == (find_len // 2):
            return True
    return False

for _ in range(10):
    map_list = [0] * 100
    tc = int(input())
    result_word_len = 0

    for i in range(100):
        map_list[i] = list(input().strip()[:])

    for k in range(100, 0, -1):
        for i in range(100):
            temp = []
            for j in range(100):
                temp += map_list[j][i]
            if find_result(temp, k) or find_result(map_list[i], k):
                result_word_len = k
                break
        if result_word_len:
            break

    print('#%d %d'%(tc, result_word_len))