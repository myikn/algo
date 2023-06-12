import sys
sys.stdin = open('input.txt')

direction = ("U", "R", "D", "L")
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
c_dir1, c_dir2 = (1, 0, 3, 2), (3, 2, 1, 0)

N, M = map(int, input().split())

# 바깥 테두리 "C"로 채운 뒤 각 줄에 입력값 대입
world = [["C"] * (M + 2) for _ in range(N + 2)]
for i in range(1, N + 1):
    row = list(input().strip())
    world[i][1:M+1] = row
R, C = map(int, input().split())

max_count, max_dir = 0, 0
flag = 0
for dir1 in range(4):
    # 시작 위치, 시작 방향, 이동 횟수
    r, c, d, count = R, C, dir1, 1

    while True:
        if world[r + dr[d]][c + dc[d]] == "C":
            break

        r += dr[d]
        c += dc[d]

        # 방향 전환
        if world[r][c] == "/":
            d = c_dir1[d]
        elif world[r][c] == "\\":
            d = c_dir2[d]
        count += 1

        # 출발 지점을 같은 방향으로 접근하면 무한히 순회함
        if (r, c, d) == (R, C, dir1):
            flag = 1
            break

    # 최대값들 갱신
    if flag:
        max_dir = dir1
        break

    if max_count < count:
        max_count = count
        max_dir = dir1


if flag:
    print(direction[max_dir])
    print("Voyager")
else:
    print(direction[max_dir])
    print(max_count)