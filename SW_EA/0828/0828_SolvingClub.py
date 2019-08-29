# S0, D1, H2, C3
def solve(data):
    cards = [13] * 4
    cards_list = {}
    result = ''
    for i in range(len(data) // 3):
        alpa = data[3 * i]
        num = int(data[3 * i + 1] + data[3 * i + 2])
        if cards_list.get(alpa):
            if num not in cards_list[alpa]:
                cards_list[alpa].append(num)
            else: return 'ERROR'
        else: cards_list[alpa] = [num]
        if alpa == 'S': alpa = 0
        elif alpa == 'D': alpa = 1
        elif alpa == 'H': alpa = 2
        else: alpa = 3
        cards[alpa] -= 1

    for card_num in cards:
        result += str(card_num) + ' '

    return result

input_data = []
for _ in range(int(input().strip())):
    input_data.append(input())

for tc_num, tc_data in enumerate(input_data):
    print("#%d" %(tc_num + 1), solve(tc_data))

'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''