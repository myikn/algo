import sys
sys.stdin = open('input.txt')


def next(x):
    return dy / dx * x - dy / dx * x_e + y_e


def distance(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1-y2)**2)**(1/2)


x_s, y_s = map(int, input().split())
x_e, y_e, dx, dy = map(int, input().split())

result = ((x_s-x_e) ** 2 + (y_s-y_e)**2)**(1/2)
x,y = x_e,y_e


if dx > 0:
    for i in range(x_e, 101):
        if distance(i, next(i), x_s, y_s) < result:
            result = distance(i, int(next(i)), x_s, y_s)
            x, y = i, int(next(i))
elif dx < 0:
    for i in range(x_e, -101, -1):
        if distance(i, next(i), x_s, y_s) < result:
            result = distance(i, int(next(i)), x_s, y_s)
            x, y = i, int(next(i))
elif dy > 0:
    for i in range(y_e, 101):
        if distance(x_e, i, x_s, y_s) < result:
            result = distance(x_e, i, x_s, y_s)
            x, y = x_e, i
else:
    for i in range(y_e, -101, -1):
        if distance(x_e, i, x_s, y_s) < result:
            result = distance(x_e, i, x_s, y_s)
            x, y = x_e, i
print(x, y)