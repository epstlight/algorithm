

test_case = int(input().strip())

for tc in range(1, test_case + 1):
    formula = list(input().strip().split())
    formula = list(reversed(formula))
    stack_list = []
    result = 0
    # print(formula)
    while formula:
        temp = formula.pop()
        if temp == '.':
            continue

        elif temp == '+' or temp == '-' or temp == '/' or temp == '*':
            if len(stack_list) < 2:
                result = 'error'
                break
            num1 = stack_list.pop()
            num2 = stack_list.pop()
            if temp == '+':
                stack_list.append(num1 + num2)
            elif temp == '-':
                stack_list.append(num2 - num1)
            elif temp == '*':
                stack_list.append(num1 * num2)
            else:
                stack_list.append(num2 / num1)

        else:
            stack_list.append(int(temp))
    if formula or len(stack_list) > 1 or result == 'error':
        print('#%d error' %(tc))
    else:
        print('#%d %d' %(tc, stack_list.pop()))

