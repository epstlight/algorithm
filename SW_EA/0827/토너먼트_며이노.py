T = int(input())
data = [None] * T
for t in range(T):
    input()
    data[t] = list(map(int, input().split()))


def game(card1, card2):
    if card1[1] == card2[1]:
        return card1
    elif (card1[1] == 1 and card2[1] ==2) or (card1[1] == 2 and card2[1] == 1):
        return sorted([card1, card2], key=lambda x: x[1])[1]
    elif (card1[1] == 2 and card2[1] == 3) or (card1[1] == 3 and card2[1] == 2):
        return sorted([card1, card2], key=lambda x: x[1])[1]
    elif (card1[1] == 3 and card2[1] == 1) or (card1[1] == 1 and card2[1] == 3):
        return sorted([card1, card2], key=lambda x: x[1])[0]

def sol(case):
    cards = list(enumerate(case))
    def divide_conquer(arr):
        # print(arr, "input arr")
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return game(arr[0], arr[1])
        else:
            n = len(arr)
            if n & 1 == 0:
                middle = len(arr) // 2
            else:
                middle = len(arr) // 2 + 1
            left = arr[:middle]
            right = arr[middle:]
            left_winner = divide_conquer(left)
            right_winner = divide_conquer(right)
            # print(left_winner, right_winner, "winner")
            return game(left_winner, right_winner)
    return divide_conquer(cards)[0] + 1


for num, case in enumerate(data):
    # print(case, 'cards')
    print("#%s" % (num + 1), sol(case))

"""
4
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
16
1 2 3 1 2 3 1 2 3 1 2 3 1
"""