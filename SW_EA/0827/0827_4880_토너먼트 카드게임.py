# 1은 가위, 2는 바위, 3은 보

def check_rss(left, right):
    # print(left, right)
    if left[1] == 1:
        if right[1] == 2:
            return right
        else:
            return left

    elif left[1] == 2:
        if right[1] == 3:
            return right
        else:
            return left
    else:
        if right[1] == 1:
            return right
        else:
            return left

def divide_conquer(temp_list):
    if len(temp_list) == 1:
        return temp_list[0]
    elif len(temp_list) == 2:
        return check_rss(temp_list[0], temp_list[1])
    else:
        temp_list_len = len(temp_list)

        # 짝수
        if not temp_list_len % 2:
            mid = temp_list_len // 2
        # # 홀수
        else:
            mid = temp_list_len // 2 + 1
        left_list = temp_list[:mid]
        right_list = temp_list[mid:]
        # print(left_list, right_list, mid)
        left_winner = divide_conquer(left_list)
        right_winner = divide_conquer(right_list)

        return check_rss(left_winner, right_winner)



for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    input_list = list(map(int, input().strip().split()))
    rss_list = list(enumerate(input_list))
    print('#%d' %(tc), divide_conquer(rss_list)[0] + 1)


