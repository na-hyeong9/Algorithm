def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = lcm*arr[i]/gcd(lcm, arr[i])
    return lcm