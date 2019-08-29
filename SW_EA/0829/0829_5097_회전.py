T = int(input().strip())
input_data = [None] * T
for t in range(T):
    input_data[t] = list(map(int, input().strip().split()))
    input_data[t].append(list(map(int, input().strip().split())))


def solve(data):
    n = data[0]
    m = data[1]
    num_list = data[2][:]
    for _ in range(m):
        num_list.append(num_list.pop(0))
    return num_list[0]


for tc, case in enumerate(input_data):
    print('#%d' %(tc + 1), solve(case))

