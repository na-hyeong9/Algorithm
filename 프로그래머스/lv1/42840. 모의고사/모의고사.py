def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    result = []
    
    for i, a in enumerate(answers):
        if a1[i % 5] == a:
            score[0] += 1
        if a2[i % 8] == a:
            score[1] += 1
        if a3[i % 10] == a:
            score[2] += 1

    for j, s in enumerate(score):
        if s == max(score):
            result.append(j + 1)

    return result