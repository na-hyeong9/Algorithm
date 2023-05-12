import math

def solution(n, a, b):
    answer = 0
    
    while True: # A와 B가 만날 때 까지 반복
        a = math.ceil(a / 2) # 올림한 값을 새로운 번호로 지정
        b = math.ceil(b / 2)
        
        answer += 1
        if a == b:
            break
    return answer