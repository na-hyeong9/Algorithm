n = int(input())
fac = 1
cnt = 0

for i in range(1, n+1):
    fac *= i

for j in reversed(list(str(fac))):
    if j == '0':
        cnt += 1
    else:
        break

print(cnt)