import math

def solution(n, stations, w):
    answer = 0
    space = w * 2 + 1 # 기지국 전파 범위
    start = 1
    
    for s in stations:
        l = s - w - start # 기지국 설치 위치 - 전파 범위 - 현재 위치 -> 전파가 닿지 않는 아파트의 길이
        if l > 0:
            answer += math.ceil(l / space) # 설치 필요한 기지국 개수
        start = s + w + 1
        
    if n >= start:
        answer += math.ceil((n - start + 1) / space)

    return answer