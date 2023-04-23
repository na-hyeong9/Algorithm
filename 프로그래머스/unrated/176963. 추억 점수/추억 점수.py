
def solution(name, yearning, photo):
    answer = []
    photo_dic = dict(zip(name, yearning))
    p = photo[0]
    
    for i in range(len(photo)):
        grade = 0
        for j in photo[i]:
            if j in photo_dic:
                grade += int(photo_dic[j])
        
        answer.append(grade)
    return answer