from collections import deque

def get_next_pos(board,  pos):
    n = len(board)
    possible = []
    pos = list(pos)
    f_pos, s_pos = pos
    fx, fy = f_pos
    sx, sy = s_pos

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 1. 평행이동
    for i in range(4):
        nfx, nfy = fx + dx[i], fy + dy[i]
        nsx, nsy = sx + dx[i], sy + dy[i]
        if 0 <= nfx < n and 0 <= nfy < n and 0 <= nsx < n and 0 <= nsy < n:
            if board[nfx][nfy] != 1 and board[nsx][nsy] != 1:
                    possible.append([(nfx, nfy), (nsx, nsy)])

    # 2. 회전이동
    # 1) 가로 => 세로
    if sx == fx:
        # (1) 아래가 비어있을때
        if 0 <= fx+1 < n and board[fx+1][fy] != 1 and board[sx+1][sy] != 1:
                possible.append([(fx, fy), (fx+1, fy)])
                possible.append([(sx+1, sy), (sx, sy)])
        # (2) 위가 비어있을때
        if 0 <= fx-1 < n and board[fx-1][fy] != 1 and board[sx-1][sy] != 1:
                possible.append([(fx-1, fy), (fx, fy)])
                possible.append([(sx-1, sy), (sx, sy)])

    # 세로? 세로 => 가로 회전!
    elif sy == fy:
        # (1) 오른쪽이 비어 있을때
        if 0 <= fy+1 < n and board[fx][fy+1] != 1 and board[sx][sy+1] != 1:
                possible.append([(fx, fy), (fx, fy+1)])
                possible.append([(sx, sy), (sx, sy+1)])
        # (2) 왼쪽이 비어 있을때
        if 0 <= fy-1 < n and board[fx][fy-1] != 1 and board[sx][sy-1] != 1:
                possible.append([(fx, fy-1), (fx, fy)])
                possible.append([(sx, sy-1), (sx, sy)])

    return possible


def solution(board):
    n = len(board)

    q = deque()
    pos = [(0, 0), (0, 1)]
    q.append((pos, 0))
    visited = [pos]

    while q:
        pos, cnt = q.popleft()
        
        if (n-1, n-1) in pos:
            return cnt

        for next_pos in get_next_pos(board, pos):    
            if next_pos not in visited:
                q.append((next_pos, cnt+1))
                visited.append(next_pos)

    return 0

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))
