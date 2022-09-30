N = int(input())
li = []

for _ in range(N):
    li.append(input())

set_li = list(set(li))

set_li.sort()
set_li.sort(key=len)

print(*set_li, sep="\n")
