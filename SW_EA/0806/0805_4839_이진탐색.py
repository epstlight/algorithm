test_case = int(input())

for tc in range(test_case):
    total_page, a_finish_page, b_finish_page = map(int, input().strip().split(' '))
    a_left = b_left = 1
    a_right = b_right = total_page
    while True:
        a_mid = (a_right + a_left) // 2
        b_mid = (b_right + b_left) // 2

        if a_mid == a_finish_page and b_mid == b_finish_page:
            print('#%d 0' %(tc + 1))
            break
        elif a_mid == a_finish_page:
            print('#%d A' % (tc + 1))
            break
        elif b_mid == b_finish_page:
            print('#%d B' % (tc + 1))
            break
        if a_mid < a_finish_page: a_left = a_mid
        else: a_right = a_mid

        if b_mid < b_finish_page: b_left = b_mid
        else: b_right = b_mid

