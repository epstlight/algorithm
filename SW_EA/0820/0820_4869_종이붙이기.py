
def dfs(n):
    if not n:
        return 1
    elif n < 0:
        return 0
    else:
        return dfs(n - 10) + 2 * dfs(n - 20)

test_case = int(input())
result_cnt = 0
for tc in range(1, test_case + 1):
    n = int(input())
    result_cnt = dfs(n)
    print('#%d %d'%(tc, result_cnt))
