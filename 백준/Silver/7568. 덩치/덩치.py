T = int(input())
li = []

for _ in range(T):
    x, y = map(int, input().split())
    li.append((x,y))

for j in li:
    rank = 1
    for k in li:
        if (j[0] <k[0]) & (j[1] <k[1]):
            rank += 1
    print(rank, end=" ")