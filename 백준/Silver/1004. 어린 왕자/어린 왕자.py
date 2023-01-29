 

import sys
input = sys.stdin.readline

T = int(input()) 
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        temp = 0
        cx, cy, r = map(int, input().split())
        if (x1-cx)**2 + (y1-cy)**2 < r**2:
            cnt += 1
            temp += 1
        if (x2-cx)**2+ (y2-cy)**2 < r**2:
            cnt += 1
            temp += 1
        if temp == 2:
            cnt -= 2

    print(cnt)