def check_bracket(a, b):
    if a == ')' and b == '(':
        return True
    elif a == '}' and b == '{':
        return True
    else:
        return False

test_case = int(input().strip())
for tc in range(1, test_case + 1):
    words = input()
    result = 1
    bracket_list = []
    for word in words:
        if word == '(' or word == ')' or word == '{' or word == '}':
            bracket_list.append(word)

    temp_list = []
    while len(bracket_list) > 1:
        temp_a = bracket_list.pop()
        temp_b = bracket_list.pop()
        if check_bracket(temp_a, temp_b):
            if temp_list:
                bracket_list.extend(temp_list[::-1])
                temp_list = []
            continue
        else:
            temp_list.append(temp_a)
            bracket_list.append(temp_b)

    if bracket_list or temp_list:
        result = 0
    print('#%d %d' %(tc, result))