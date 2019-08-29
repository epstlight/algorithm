def my_append(my_list, value):
    M = len(my_list)
    new_list = [0] * (M + 1)
    for i in range(M):
        new_list[i] = my_list[i]
    new_list[M] = value
    return new_list

def my_pop(my_list):
    M = len(my_list)
    new_list = [0] * (M - 1)
    for i in range(M - 1):
        new_list[i] = my_list[i]
    return new_list, my_list[M - 1]

def max_box(box_list):
    max_list = [0]
    max_num = box_list[0]
    for i in range(1, len(box_list)):
        if max_num == box_list[i]:
            max_list = my_append(max_list, i)
        elif max_num < box_list[i]:
            max_num = box_list[i]
            max_list = [i]
    return max_list


def min_box(box_list):
    min_list = [0]
    min_num = box_list[0]
    for i in range(1, len(box_list)):
        if min_num == box_list[i]:
            min_list = my_append(min_list, i)
        elif min_num > box_list[i]:
            min_num = box_list[i]
            min_list = [i]
    return min_list

for tc in range(10):
    dump_num = int(input())
    box_list = list(map(int, input().strip().split(' ')))
    max_list = []
    min_list = []
    while dump_num > 0:
        if max_list == []: max_list = max_box(box_list)
        if min_list == []: min_list = min_box(box_list)

        max_list, max_i = my_pop(max_list)
        min_list, min_i = my_pop(min_list)
        box_list[max_i] -= 1
        box_list[min_i] += 1
        dump_num -= 1

    if max_list == []: max_list = max_box(box_list)
    if min_list == []: min_list = min_box(box_list)

    diff = box_list[max_list[0]] - box_list[min_list[0]]
    print('#%d %d' %(tc + 1, diff))
