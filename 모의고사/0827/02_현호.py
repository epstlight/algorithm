T = int(input())
data = [None] * T
for t in range(T):
    n = int(input())
    data[t] = [list(map(int, input().split())) for _ in range(n)]


def scaling(cards):
    new_cards = []
    for card in cards:
        location = (card[0] * 2) + 2000, (card[1] * 2) + 2000
        new_cards.append((location, card[2], card[3]))
    return new_cards


def sol(case):
    cards = scaling(case)
    total_energy = 0
    while cards:
        # print(cards)
        new_cards = []
        n = len(cards)
        for i in range(n):
            location, direction, energy = cards[i]
            if direction == 0:
                if location[1] + 1 < 4002:
                    new_cards.append(((location[0], location[1] + 1), direction, energy))
            elif direction == 1:
                if location[1] - 1 >= 0:
                    new_cards.append(((location[0], location[1] - 1), direction, energy))
            elif direction == 2:
                if location[0] - 1 >= 0:
                    new_cards.append(((location[0] - 1, location[1]), direction, energy))
            else:
                if location[0] + 1 < 4002:
                    new_cards.append(((location[0] + 1, location[1]), direction, energy))

        dic = {}
        for location, direction, energy in new_cards:
            if dic.get(location):
                dic[location].append((direction, energy))
            else:
                dic[location] = [(direction, energy)]

        cards = []
        for key, value in dic.items():
            if len(value) > 1:
                # print(key, value)
                for direction, energy in value:
                    total_energy += energy
            else:
                cards.append((key, value[0][0], value[0][1]))

    return total_energy


for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))

"""
1
14
-6 5 3 1
-3 5 2 1
-5 2 1 1
3 5 3 1
5 7 1 1
6 7 3 1
7 5 2 1
5 3 0 1
-4 -4 1 1
-4 -6 0 1
5 -3 2 1
4 -6 0 1
6 -4 1 1
9 -7 2 1
"""