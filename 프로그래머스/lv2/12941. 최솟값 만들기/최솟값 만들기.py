def solution(A,B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B)
    for a, b in zip(A, B):
        answer += a*b
    return answer
                