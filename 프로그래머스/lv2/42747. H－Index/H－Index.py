def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations),-1,-1):
        if len([j for j in citations if j >= i]) >= i:
            answer = i
            break
    return answer