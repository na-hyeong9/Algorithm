def solution(k, m, score):
    score.sort()

    sum = 0
    for pack in range(len(score),m-1, -m):
        sum += score[pack-m]*m
    return sum