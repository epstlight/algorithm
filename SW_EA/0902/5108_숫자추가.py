

for tc in range(1, int(input().strip())+1):
    n, m, l = map(int, input().strip().split())
    num_list = list(map(int, input().strip().split()))

    for _ in range(m):
        idx, value = map(int, input().strip().split())
        num_list.insert(idx, value)

    print('#%d' %(tc), num_list[l])