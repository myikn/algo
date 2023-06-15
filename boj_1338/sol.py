import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
x, y = map(int, input().split())
result = []

if a > b:
    a, b = b, a

if y >= abs(x) or y < 0:
    print('Unknwon Number')

else:
    x = abs(x)
    value = x * (a // x) + y
    flag = True
    while value <= b:
        if a <= value <= b:
            if result:
                flag = False
                break
            result.append(value)
        value += x
    if flag and result:
        print(*result)
    else:
        print('Unknwon Number')