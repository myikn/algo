# 다음과 같은 귀납적인 규칙에 의해서 만들어지는 무한한 크기의 이진 트리를 생각하자. 각각의 노드에는 두 정수의 순서쌍이 할당되어 있다.
#
# 루트에는 (1, 1)이 할당된다.
# 어떤 노드가 (a, b)가 할당되었을 때, 그 노드의 왼쪽 자식에는 (a+b, b)가 할당되고, 오른쪽 자식에는 (a, a+b)가 할당된다.
# 우리는 어떤 노드가 주어졌을 때, 루트에서 그 노드로 이동하는 최단 경로를 찾으려 한다. 하지만 최단 경로가 매우 길 수도 있기 때문에, 왼쪽 자식으로 이동하는 회수와 오른쪽 자식으로 이동하는 회수를 찾으려고 한다.
#
# 입력으로 두 정수 A, B가 주어졌을 때, 루트에서 (A, B)가 할당된 노드까지 최단 경로로 이동할 때, 왼쪽 자식으로 이동하는 회수와 오른쪽 자식으로 이동하는 회수를 구해내는 프로그램을 작성하시오.


# 풀이방법
# a 혹은 b가 1인 경우 현재 노드에서 오른쪽 혹은 왼쪽 직선으로만 내려가게됨
# 그 밖에 a, b 값의 차이에 따라서 왼쪽 오른쪽으로 움직이면서 카운트
import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
x, y = 0, 0
while True:
    if a == 1:
        y += b - 1
        break
    elif b == 1:
        x += a - 1
        break
    if a < b:
        b -= a
        y += 1
    else:
        a -= b
        x += 1
print(x, y)