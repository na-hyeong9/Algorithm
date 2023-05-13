def solution(people, limit):
    people.sort() # 사람들의 몸무게를 오름차순으로 정렬
    count = 0 # 구명보트의 수를 카운트하는 변수
    left, right = 0, len(people) - 1 # 인덱스를 이용해 가장 가벼운 사람과 무거운 사람을 가리킴
    
    while left <= right:
        if people[left] + people[right] <= limit: # 가장 가벼운 사람과 무거운 사람의 무게 합이 제한 무게 이하인 경우
            left += 1 # 가장 가벼운 사람은 구명보트에 탑승했으므로 다음 사람을 가리키도록 인덱스 증가
        right -= 1 # 가장 무거운 사람은 구명보트에 탑승했으므로 다음 사람을 가리키도록 인덱스감소
        count += 1 # 구명보트의 수를 증가시킴
    
    return count
