def solution(x):
    answer = True
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)
    
    if int(x)%sum == 0:
        return answer
    else:
        return False