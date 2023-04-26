def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    
    for i in A:
        for j in B:
            # i와 j를 비교해서 j가 더 클경우 answer에 +1 j는 사용했으므로 삭제
            if i < j:
                answer += 1
                B.remove(j)
                break
    return answer