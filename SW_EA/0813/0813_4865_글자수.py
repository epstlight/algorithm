
testcase = int(input())

for tc in range(testcase):
    str1 = input()
    str2 = input()

    words_dict = {}
    for word in str2:
        if word in str1:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
    print('#%d %d' %(tc + 1, max(words_dict.values())))