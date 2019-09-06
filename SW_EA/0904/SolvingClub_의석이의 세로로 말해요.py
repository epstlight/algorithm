T = int(input().strip())
input_data = [[] for _ in range(T)]
for t in range(T):
    for _ in range(5):
        input_data[t].append(list(a for a in input().strip()))

def solve(data):
    result_list = []
    data_empty = [False] * 5
    while False in data_empty:
        for i in range(5):
            if data[i]:
                result_list.append(data[i].pop(0))
            elif not data[i] and not data_empty[i]:
                data_empty[i] = True
    return ''.join(result_list)

for tc, case in enumerate(input_data, 1):
    print('#%d' %tc, solve(case))