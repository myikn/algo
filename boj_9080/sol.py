import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    tmp = input().split()
    hour = int(tmp[0].split(":")[0])
    minute = int(tmp[0].split(":")[1])
    time = int(tmp[1])

    result = 0
    while time > 0:
        if (hour >= 22 or hour < 3) and time > 300:
            while hour != 8:
                hour = (hour + 1) % 24
                time -= 60
            result += 5000
            time += minute
            minute = 0
        else:
            hour = (hour + 1) % 24
            result += 1000
            time -= 60

    print(str(result))