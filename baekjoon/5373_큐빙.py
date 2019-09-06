#시뮬레이션
#U: 윗 면 0, D: 아랫 면1, F: 앞 면 2, B: 뒷 면3, L: 왼쪽 면4, R: 오른쪽 면5
#+ 시계 - 반시계
#흰색은 w, 노란색은 y, 빨간색은 r, 오렌지색은 o, 초록색은 g, 파란색은 b.
def nineteen_rotate(cube_list, direct):
    temp_list = []
    for colors in cube_list: temp_list.append(colors[:])
    for y in range(3):
        for x in range(3):
            if direct == 0:
                cube_list[x][2-y] = temp_list[y][x]
            else:
                cube_list[2-x][y] = temp_list[y][x]

def rotate(plane, direct):
    if plane == 'U':
        if direct == '+':
            cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[5][0][:], cube[2][0][:], cube[4][0][:], cube[3][0][:]
            nineteen_rotate(cube[0], 0)
        else:
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = cube[4][0][:], cube[2][0][:], cube[5][0][:], cube[3][0][:]
            nineteen_rotate(cube[0], 1)

    elif plane == 'D': # 2, 5, 3, 4 = 4, 2, 5, 3 // 2, 4, 3, 5 = 5, 2, 4, 3(XY = 2)
        if direct == '+':
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = cube[4][2][:], cube[2][2][:], cube[5][2][:], cube[3][2][:]
            nineteen_rotate(cube[1], 0)
        else:
            cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[5][2][:], cube[2][2][:], cube[4][2][:], cube[3][2][:]
            nineteen_rotate(cube[1], 1)

    elif plane == 'F': # 0, 5, 1, 4 = 4, 0, 5, 1 // 0, 4, 1, 5 = 5, 0, 4, 1
        if direct == '+':
            temp = cube[0][2][:]
            for i in range(3):
                cube[0][2][i] = cube[4][2-i][2]
                cube[4][2-i][2] = cube[1][0][2-i]
                cube[1][0][2-i] = cube[5][i][0]
                cube[5][i][0] = temp[i]
            nineteen_rotate(cube[2], 0)
        else:
            temp = cube[0][2][:]
            for i in range(3):
                cube[0][2][i] = cube[5][i][0]
                cube[5][i][0] = cube[1][0][2-i]
                cube[1][0][2-i] = cube[4][2-i][2]
                cube[4][2-i][2] = temp[i]
            nineteen_rotate(cube[2], 1)

    elif plane == 'B':
        if direct == '+':
            temp = cube[0][0][:]
            for i in range(3):
                cube[0][0][i] = cube[5][i][2]
                cube[5][i][2] = cube[1][2][2-i]
                cube[1][2][2-i] = cube[4][2-i][0]
                cube[4][2-i][0] = temp[i]
            nineteen_rotate(cube[3], 0)

        else:
            temp = cube[0][0][:]
            for i in range(3):
                cube[0][0][i] = cube[4][2-i][0]
                cube[4][2-i][0] = cube[1][2][2-i]
                cube[1][2][2-i] = cube[5][i][2]
                cube[5][i][2] = temp[i]
            nineteen_rotate(cube[3], 1)

    elif plane == 'L':

        if direct == '+':
            for i in range(3):
                temp = cube[0][i][0]
                cube[0][i][0] = cube[3][2-i][2]
                cube[3][2-i][2] = cube[1][i][0]
                cube[1][i][0] = cube[2][i][0]
                cube[2][i][0] = temp
            nineteen_rotate(cube[4], 0)
        else:
            for i in range(3):
                temp = cube[0][i][0]
                cube[0][i][0] = cube[2][i][0]
                cube[2][i][0] = cube[1][i][0]
                cube[1][i][0] = cube[3][2-i][2]
                cube[3][2-i][2] = temp
            nineteen_rotate(cube[4], 1)
    elif plane == 'R':
        if direct == '+':
            for i in range(3):
                temp = cube[0][i][2]
                cube[0][i][2] = cube[2][i][2]
                cube[2][i][2] = cube[1][i][2]
                cube[1][i][2] = cube[3][2-i][0]
                cube[3][2-i][0] = temp
            nineteen_rotate(cube[5], 0)
        else:
            for i in range(3):
                temp = cube[0][i][2]
                cube[0][i][2] = cube[3][2-i][0]
                cube[3][2-i][0] = cube[1][i][2]
                cube[1][i][2] = cube[2][i][2]
                cube[2][i][2] = temp
            nineteen_rotate(cube[5], 1)




for _ in range(int(input().strip())):
    cube = []
    cube.append([['w'] * 3 for _ in range(3)])
    cube.append([['y'] * 3 for _ in range(3)])
    cube.append([['r'] * 3 for _ in range(3)])
    cube.append([['o'] * 3 for _ in range(3)])
    cube.append([['g'] * 3 for _ in range(3)])
    cube.append([['b'] * 3 for _ in range(3)])

    n = int(input().strip())
    rotate_command = input().strip().split()
    for i in range(n):
        rotate(rotate_command[i][0], rotate_command[i][1])
        # for colors in cube[0]:
        #     print(''.join(colors))
        # print()
    for colors in cube[0]:
        print(''.join(colors))