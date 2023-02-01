import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = {}
for i in range(n):
    inp = input().rstrip()
    data[i+1] = inp
    data[inp] = i+1
    
for i in range(m):
    inp = input().rstrip()
    if inp.isdigit():
        print(data[int(inp)])
    else:
        print(data[inp])