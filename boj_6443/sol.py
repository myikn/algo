import sys
sys.stdin = open('input.txt')


def back(checklist, idx):
    if len(checklist) == len(wordlist[idx]):
        print(''.join(checklist))
        return

    for k in check[idx]:
        if check[idx][k]:
            checklist.append(k)
            check[idx][k] -= 1

            back(checklist, idx)

            checklist.pop()
            check[idx][k] += 1


N = int(input())
check = []
wordlist = []

for i in range(N):
    word = sorted(input())
    wordlist.append(word)
    visited = {}

    for j in word:
        if j in visited:
            visited[j] += 1
        else:
            visited[j] = 1

    check.append(visited)

for i in range(N):
    back([], i)