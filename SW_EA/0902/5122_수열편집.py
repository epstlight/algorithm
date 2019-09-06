

for tc in range(1, int(input().strip()) + 1):
    n, m, l = map(int, input().strip().split())
    num_list = list(map(int, input().strip().split()))

    for _ in range(m):
        command = input().strip().split()
        if command[0] == 'I':
            num_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'D':
            num_list.pop(int(command[1]))
        elif command[0] == 'C':
            num_list[int(command[1])] = int(command[2])

    if len(num_list) - 1 < l:
        print('#%d -1' %(tc))
    else:
        print('#%d' % (tc), num_list[l])
