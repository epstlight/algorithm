
testcase = int(input())

for tc in range(testcase):
    str1 = input()
    str2 = input()

    for i in range(len(str2)- len(str1) + 1):
        if str1 == str2[i:(i+len(str1))]:
            print('#%d 1' %(tc + 1))
            break
    else:
        print('#%d 0' %(tc + 1))
