import itertools

def solution(number):
    answer = 0
    com = list(itertools.combinations(number, 3))
    for sam in com:
        if sum(sam) == 0:
            answer += 1
    return answer