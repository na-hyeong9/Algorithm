a, b = map(int, input().split())
listen = set()
see = set()

for i in range(a):
    listen.add(input())

for j in range(b):
    see.add(input())

li = sorted(list(listen&see))

print(len(li))
print(*li,sep='\n')