from collections import Counter

def solution(participant, completion):
    answer = ''
    participant_cnt = Counter(participant)
    completion_cnt = Counter(completion)
    
    answer = participant_cnt - completion_cnt
    
    return list(answer.keys())[0]