N, K = map(int, input().split()) 
li = list()
for i in range(N):
    li.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//li[i]
    K = K%li[i]

print(count)