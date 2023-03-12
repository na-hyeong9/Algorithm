def solution(lottos, win_nums):
    cnt_corr = 0
    cnt_zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt_corr += 1
        if lotto == 0:
            cnt_zero += 1
            
    total = cnt_corr + cnt_zero

    rank = {6 : 1,
            5 : 2,
            4 : 3,
            3 : 4,
            2 : 5,
            1 : 6,
            0 : 6}
    
    return [rank[total],rank[cnt_corr]]