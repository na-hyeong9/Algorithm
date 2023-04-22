from itertools import permutations

#소수 판별 함수
def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers)+1) :
        nums.append(list(set(map(''.join, permutations(numbers, i))))) # 모든 조합
    per = list(set(map(int, set(sum(nums, []))))) # per 배열에 해당 조합들을 합쳐서 int형으로 저장
    
    for p in per :
        if is_prime_number(p) == True :
            answer += 1

    return answer