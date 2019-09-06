T = int(input().strip())
input_data = [None] * T
for t in range(T):
    input()
    input_data[t] = list(map(int, input().strip().split()))

def check_danjo(num):
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            return False
    return True

def solve(data):
    max_danjo = -1
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            before_check = data[i] * data[j]
            if max_danjo < before_check  and check_danjo(before_check):
                max_danjo = before_check
    return max_danjo

for tc, case in enumerate(input_data, 1):
    print('#%d' %tc, solve(case))