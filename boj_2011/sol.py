import sys
sys.stdin = open('input.txt')

n = input()
dp = [0 for _ in range(len(n) + 1)]

if n[0] == '0':
    print('0')

else:
    dp[0] = 1
    dp[1] = 1

    # dp의 인덱스와 n의 인덱스를 맞춰줌
    n = '0' + n
    for i in range(2, len(n)):
        # i번째 숫자가 단독으로 존재하는 경우
        if n[i] > '0':
            dp[i] += dp[i - 1]
        # i번째 숫자가 결합해서 존재하는 경우
        if n[i - 1] != '0' and n[i - 1] + n[i] < '27':
            dp[i] += dp[i - 2]

    print(dp[len(n) - 1] % 1000000)