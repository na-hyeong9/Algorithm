def solution(board):
    max_point = 0
    w, h = len(board[0]), len(board)
    
    count = 0
    for b in board: #모든 요소가 0일때 -> 0 반환
        count += b.count(0)
    if count == w*h:
        return 0
    
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] == 0:
                continue
            else:
                min_point = min(board[i-1][j-1],board[i][j-1],board[i-1][j])
                board[i][j] = min_point + 1
                if max_point < board[i][j]:
                    max_point = board[i][j]
                    
    if max_point == 0:
        return 1
    return max_point ** 2