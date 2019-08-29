test_case = int(input())

for tc in range(test_case):
    card_num = int(input())
    card_cnt = [0] * 10
    cards = input()

    for card in cards:
        card_cnt[int(card)] += 1

    max_card_cnt = card_cnt[0]
    max_card_num = 0
    for i in range(1, 10):
        if max_card_cnt <= card_cnt[i]:
            max_card_cnt = card_cnt[i]
            max_card_num = i

    print('#%d %d %d' %(tc + 1, max_card_num, max_card_cnt))