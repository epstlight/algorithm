# n극 상단 1, s극 하단 2
def find_magnetic(x, n):
    cnt = 0
    double = False
    for y in range(n):
        if magnetic_list[y][x] == 1 and not double:
            double = True
        elif magnetic_list[y][x] == 2 and double:
            double = False
            cnt += 1
    return cnt


for tc in range(1, 11):
    n = int(input().strip())
    magnetic_list = list(list(map(int, input().strip().split())) for _ in range(n))
    magnetic_cnt = 0

    for i in range(n):
        magnetic_cnt += find_magnetic(i, n)

    print("#%d %d" %(tc, magnetic_cnt))


