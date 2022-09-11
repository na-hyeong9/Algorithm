n, m = map(str, input().split())

N = int(n[::-1])
M = int(m[::-1])

if M < N:
    print(N)
else:
    print(M)