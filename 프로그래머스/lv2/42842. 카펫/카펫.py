def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 : # 노란색의 수가 i로 나누어 떨어지면
            yellow_x = int(yellow/i) # 가로는 노란색 나누기 i
            yellow_y = i # 세로는 i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
    
    return answer
