testcase = int(input())

for tc in range(testcase):
    words_num = int(input().strip().split()[1])
    words_list = list(map(str, input().strip().split()))
    words_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
                  'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    words_cnt = [[0] * 2 for _ in range(10)]
    for i in range(10):
        for key, value in words_dict.items():
            if value == i:
                words_cnt[i][0] = key
                break

    for word in words_list:
        words_cnt[words_dict[word]][1] += 1

    print('#%d' %(tc + 1))
    for i in range(10):
        if words_cnt[i][1]:
            temp = (words_cnt[i][0] + ' ') * words_cnt[i][1]
            print(temp, end='')
    print()

