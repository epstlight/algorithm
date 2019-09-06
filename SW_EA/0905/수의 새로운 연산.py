

for tc in range(1, int(input().strip()) + 1):
    p, q = map(int, input().strip().split())
    current = 1
    num_list = [(1, 1)]
    start_y = 1

    while current < max(p, q):
        current += 1
        if num_list[-1][0] == start_y:
            start_y += 1
            num_list.append((1, start_y))
        else:
            num_list.append((num_list[-1][0] + 1, num_list[-1][1] - 1))
    find_x, find_y = num_list[p-1][0] + num_list[q-1][0], num_list[p-1][1] + num_list[q-1][1]

    num = dxy = 1
    while find_y > 1:
        find_y -= 1
        num += dxy
        dxy += 1
    while find_x > 1:
        find_x -= 1
        dxy += 1
        num += dxy

    print('#%d' %tc, num)