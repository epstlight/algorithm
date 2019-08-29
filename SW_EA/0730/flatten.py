
for tc in range(10):
    dump_num = int(input())
    box_list = list(map(int, input().strip().split(' ')))
    temp_max = temp_min = -1

    while dump_num >= 0:
        max_i = min_i = 0
        max_value = 0
        min_value = 100
        cnt_max = cnt_min = False
        for i in range(100):
            if max_value < box_list[i] and not cnt_max :
                max_value = box_list[i]
                max_i = i
                if temp_max == max_value:
                    cnt_max = True
            if min_value > box_list[i] and not cnt_min:
                min_value = box_list[i]
                min_i = i
                if temp_min == min_value:
                    cnt_min = True
            if cnt_min and cnt_max:
                break

        box_list[max_i] -= 1
        box_list[min_i] += 1
        temp_min = min_value
        temp_max = max_value
        dump_num -= 1

    diff = max_value - min_value
    print('#%d %d' %(tc + 1, diff))

