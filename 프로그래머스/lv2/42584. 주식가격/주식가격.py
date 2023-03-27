from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        sec = 0
        price = prices.popleft()
        for p in prices:
            sec += 1
            if p >= price:
                continue
            else:
                break
        answer.append(sec)
            
    return answer