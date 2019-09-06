#r c s 속력 d 이동방향 z 크기 크기 기준으로 삭제

r, c, m = map(int, input().strip().split())

dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
fiserman = 0
fish_stack = []
for _ in range(m):
    fish_stack.append(tuple(map(int, input().strip().split())))
result_sum_fish = 0

while True:
    fiserman += 1
    fiserman_min_r = r + 1
    fiserman_min_r_index = len(fish_stack)

    #한마리 잡아 넣기
    for i in range(len(fish_stack)):
        if fish_stack[i][1] == fiserman and fish_stack[i][0] < fiserman_min_r:
            fiserman_min_r = fish_stack[i][0]
            fiserman_min_r_index = i
    if fiserman_min_r != r + 1:
        result_sum_fish += fish_stack.pop(fiserman_min_r_index)[-1]

    if fiserman == c:
        break

    # 물고기 이동하기
    # 1 위, 2 아래, 3 오른쪽, 4왼쪽
    dict = {}
    for i in range(len(fish_stack)):
        y, x, s, d, size = fish_stack[i]
        speed = s
        while speed > 0:
            if d < 3:
                y += dy[d]
                if not y and d == 1:
                   y, d = 2, 2
                elif y == r + 1 and d == 2:
                    y, d = r - 1, 1
            else:
                x += dx[d]
                if not x and d == 4:
                    x, d = 2, 3
                elif x == c + 1 and d == 3:
                    x, d = c - 1, 4
            speed -= 1

        if dict.get((y, x)):
            dict[(y, x)].append((s, d, size))
        else:
            dict[(y, x)] = [(s, d, size)]

    # 동일 좌표 물고기 삭제
    fish_stack = []
    for key, value in dict.items():
        if len(value) > 1:
            value = sorted(value, key=lambda x:x[-1])
            s, d, size = value[-1]
        else:
            s, d, size = value[0]
        y, x = key
        fish_stack.append((y, x, s, d, size))

print(result_sum_fish)

