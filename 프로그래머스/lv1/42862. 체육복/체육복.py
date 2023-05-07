def solution(n, lost, reserve):    
    lost_li = list(set(lost) - set(reserve))
    reserve_li = list(set(reserve) - set(lost)) # 중복 제거
    
    for r in reserve_li:
        before = r-1
        after = r+1
        
        if before in lost_li:
            lost_li.remove(before)
        elif after in lost_li:
            lost_li.remove(after)
                
    return n - len(lost_li) # 총 인원 - 못 빌린 인원