def solution(s):
    answer = []
    s = s[2:-2] # 앞뒤 {{}} 제외한 리스트
    s = s.split("},{") # 나머지 '}',와 '{'를 제외한 리스트
    s.sort(key = len) # 길이를 기준으로 오름차순
    for sl in s:
        sl = sl.split(',') # ',' 기준으로 리스트
        for l in sl:
            if int(l) not in answer: # 없으면 answer 리스트에 추가
                answer.append(int(l))
    return answer