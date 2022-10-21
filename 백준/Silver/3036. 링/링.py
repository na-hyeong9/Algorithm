import sys

input = sys.stdin.readline


def gcd(a, b):
    if a > b:
        pass
    else:
        a, b = b, a

    while b > 0:
        r = a % b
        a, b = b, r

    return a


n = int(input())
rings = list(map(int, input().split()))
first = rings[0]

for i, ring in enumerate(rings):
    if i == 0: continue
    g = gcd(first, ring)
    print(first // g, '/', ring // g, sep='')