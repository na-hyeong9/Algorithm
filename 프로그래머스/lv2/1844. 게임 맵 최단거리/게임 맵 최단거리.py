from collections import deque
 
def bfs(maps, x, y):
	# 다음에 방문할 지점 저장
    next_visit = deque()
    next_visit.append([x, y])
    # 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 방문 시작
    while next_visit:
        x, y = next_visit.popleft()
        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문 가능한 경우
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 0:
                # 아직 방문하지 않은 경우
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    # 다음에 방문할 지점으로 선택
                    next_visit.append([nx, ny])
    # 방문 불가능한 경우 -1로 반환
    return maps[-1][-1] if maps[-1][-1] > 1 else -1 
    
    
def solution(maps):
    return bfs(maps, 0, 0)