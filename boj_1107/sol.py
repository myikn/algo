import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())

if M != 0:
    num_list = list(input().split())
else:
    num_list = []

result = abs(100 - N)
for i in range(1000001):
    for j in str(i):
        if j in num_list:
            break
    else:
        result = min(result, len(str(i)) + abs(i - N)) #min(기존답, 숫자 버튼 클릭 수 + '+/-' 버튼 클릭 수)

print(result)