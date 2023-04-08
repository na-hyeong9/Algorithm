def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)} # 방향을 dictionary(좌표)로 지정하여 문자에 따라 cur_x와 cur_y에 더해줌. 
    road = set() # 같은 좌표는 set 처리되며 중복 삭제
    cur_x, cur_y = (0,0) # 현재 위치를 저장할 변수
    
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5: # 좌표 평면의 경계
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y)) #출발지점과 도착지점이 반대여도 같은 선이기에 예외 처리
            cur_x, cur_y = next_x, next_y # 현재 위치 변경

    return len(road) // 2