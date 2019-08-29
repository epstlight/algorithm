# 상(0), 하(1), 좌(2), 우(3)
dx = [0, 0, -0.5, 0.5]
dy = [-0.5, 0.5, 0, 0]

for tc in range(1, int(input().strip()) + 1):
    n = int(input())  #원자 수
    atom_list = [[0] * 4 for _ in range(n)]     #원자를 받을 list
    result_power = 0    #결과 값

    #원자 정보 저장
    for i in range(n):
        x, y, direc, k = map(int, input().strip().split())
        atom_list[i][0], atom_list[i][1], atom_list[i][2], atom_list[i][3] = x + 1000, -y + 1000, direc, k

    while atom_list:
        dic = {}
        for i in range(len(atom_list)):
            x, y, direc, k = atom_list[i]
            x, y = x + dx[direc], y + dy[direc]
            if x < 0 or y < 0 or x > 2000 or y > 2000: continue
            else:
                if dic.get((x, y)):
                    dic[(x, y)].append((direc, k))
                else:
                    dic[(x, y)] = [(direc, k)]

        # for x, y, direc, k in next_atom:
        #     if dic.get((x, y)):
        #         dic[(x, y)].append((direc, k))
        #     else:
        #         dic[(x, y)] = [(direc, k)]

        atom_list = []
        for key, value in dic.items():
            if len(dic[key]) > 1:
                for direc, k in dic[key]:
                    result_power += k
            else:
                atom_list.append([key[0], key[1], value[0][0], value[0][1]])

    print('#%d %d' %(tc, result_power))
