N = int(input())
B = []

for _ in range(N):
    x, y = map(int, input().split())
    B.append((x,y))

for i in B:
    rank = 1
    for j in B:
        if i[0] < j[0] and i[1] < j[1]: #조건
            rank+=1
    print(rank, end = " ")