a, b = map(int,input().split())
c = int(input())
n = int(input())
r = 1 
if a*n+b <= c*n and c>=a:
    print(r)
else:
    print(0)