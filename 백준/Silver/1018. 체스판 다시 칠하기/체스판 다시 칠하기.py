
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
 
print(min(result))