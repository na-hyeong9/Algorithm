def solution(n):
    # 경우의 수 저장
    DP = [1, 2]
    for i in range(2, n):
        DP.append((DP[i - 2] + DP[i - 1]) % 1000000007)
    return DP[n - 1] % 1000000007