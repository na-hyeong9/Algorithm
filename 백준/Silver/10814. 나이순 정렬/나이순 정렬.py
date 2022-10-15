T= int(input())
li = []

for _ in range(T):
    a, n = map(str, input().split())
    a = int(a)
    li.append((a, n))

li.sort(key = lambda x : x[0])

for i in li:
    print(i[0], i[1])