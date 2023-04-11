from collections import defaultdict

def solution(genres, plays):
    answer = []
    G = defaultdict(int) # 장르별 재생 횟수 저장
    detail = defaultdict(list) # 장르별 재생된 노래를 저장 (재생 횟수, 고유 번호)
    for idx, [g, p] in enumerate(zip(genres, plays)):
        G[g] += p
        detail[g].append((p, idx))
    for g, _ in sorted(G.items(), key=lambda x: -x[1]): # 많이 재생된 순으로 정렬
        for _, i in sorted(detail[g], key=lambda x: -x[0])[:2]: # 2개 까지만 수록
            answer.append(i)
    return answer