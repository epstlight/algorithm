
test_case = int(input().strip())

for tc in range(1, test_case + 1):
    words = list(char for char in input())
    lenght = 0
    while words:
        lenght = len(words)
        for i in range(1, lenght):
            if words[i - 1] == words[i]:
                words = words[:i-1:] + words[i+1::]
                break
        else:
            break

    if not words:
        lenght = 0
    print('#%d %d' % (tc, lenght))