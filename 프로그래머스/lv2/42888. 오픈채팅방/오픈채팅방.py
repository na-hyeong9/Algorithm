def solution(record):
    answer = []
    user = dict()
    actions = []
    
    for event in record: 
        info = event.split() # record를 순회하며 각 정보를 저장
        action, userid = info[0], info[1]
        if action in ("Enter", "Change"): # leave일 땐 닉네임 정보가 없음으로 제외
            nickname = info[2]
            user[userid] = nickname # 딕셔너리 형태로 id와 nickname 저장 > id를 찾아 수정된 최종 nickname 출력
        actions.append((action, userid))
        
    for a in actions:
        action, userid = a[0], a[1]
        if action == 'Enter':
            answer.append(f'{user[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user[userid]}님이 나갔습니다.')
    
    return answer