def solution(cacheSize, cities):
    answer = 0  # 총 처리 시간을 저장하는 변수
    cache = []  # 캐시를 나타내는 리스트
    
    if cacheSize != 0:
        for city in cities:
            city = city.lower()  # 도시 이름을 소문자로 변환하여 통일
            
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1  # 처리 시간을 1 증가
            else:  # 도시가 캐시에 존재하지 않는 경우
                if len(cache) >= cacheSize:  # 캐시가 꽉 찬 경우
                    cache.pop(0)  # 캐시의 맨 앞 요소를 제거
                    
                cache.append(city)  # 도시를 캐시의 맨 뒤에 추가
                answer += 5  # 처리 시간을 5 증가
    else:  # 캐시 크기가 0인 경우
        answer += len(cities) * 5  # 처리 시간을 도시 개수에 5를 곱한 값으로 설정
                
    return answer