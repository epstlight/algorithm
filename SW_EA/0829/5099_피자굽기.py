T = int(input().strip())
input_data = [None] * T
for t in range(T):
    input_data[t] = list(map(int, input().strip().split()))
    input_data[t].append(list(map(int, input().strip().split())))

def solve(data):
    size, num, pizza_list = data[0], data[1], list(enumerate(data[2], 1))
    oven = [(0, 0)] * size
    while num > 1:
        pizza_num, cheeze = oven.pop(0)
        if not pizza_num:
            if pizza_list: oven.append(pizza_list.pop(0))
        else:
            cheeze //= 2
            if cheeze:
                oven.append((pizza_num, cheeze))
            else:
                if pizza_num: num -= 1
                if pizza_list: oven.append(pizza_list.pop(0))

    last_num = oven.pop(0)[0]
    return last_num


for tc, case in enumerate(input_data):
    print('#%d' %(tc + 1), solve(case))
