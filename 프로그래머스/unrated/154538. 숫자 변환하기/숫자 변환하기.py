def solution(x, y, n):
    answer = 0
    memo= [1e9] * (y+1)
    memo[x] = 0
    for i in range (x, y+1):
        if memo[i] == 1e9:
            continue
        if i + n <= y:
            memo[i+n] = min(memo[i+n], memo[i] + 1)
        if i * 2 <= y:
            memo[i*2] = min(memo[i*2], memo[i] + 1)
        if i * 3 <= y:
            memo[i*3] = min(memo[i*3], memo[i] + 1)
    
    if memo[y] == 1e9:
        return -1
    return memo[y]