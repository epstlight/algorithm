for i in range(1, 11):
    L = int(input())
    results = []
    arr = list(input())
    stack = [0] * L
    top = -1

    for a in arr:
        if a == '+':
            while True:
                cal, level = stack[top]
                if level < 1:
                    break
                results += cal
                top -= 1
            stack[top + 1] = a, 1
            top += 1
        elif a == '*':
            while True:
                cal, level = stack[top]
                if level < 2:
                    break
                results += cal
                top -= 1
            stack[top + 1] = a, 2
            top += 1
        elif a == '(':
            stack[top + 1] = a, 0
            top += 1
        elif a == ')':
            while True:
                cal, level = stack[top]
                if cal == '(':
                    top -= 1
                    break
                results += cal
                top -= 1
        else:
            results += a
    stack_r = [0] * L
    top_r = -1
    for b in results:
        if b == '+':
            num2 = stack_r[top_r]
            top_r -= 1
            num1 = stack_r[top_r]
            top_r -= 1
            stack_r[top_r + 1] = num1 + num2
            top_r += 1
        elif b == '*':
            num2 = stack_r[top_r]
            top_r -= 1
            num1 = stack_r[top_r]
            top_r -= 1
            stack_r[top_r + 1] = num1 * num2
            top_r += 1
        else:
            stack_r[top_r + 1] = int(b)
            top_r += 1

    print('#{0} {1}'.format(i, stack_r[top_r]))