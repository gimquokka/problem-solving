from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    (x1, y1), (x2, y2) = pos
    # 상하좌우 이동을 위한 변수선언
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 1. 상하좌우 이동
    for i in range(4):
        if board[x1+dx[i]][y1+dy[i]] == 0 and board[x2+dx[i]][y2+dy[i]] == 0:
            next_pos.append({(x1+dx[i], y1+dy[i]), (x2+dx[i], y2+dy[i])})

    # 세로 => 가로 회전
    if y1 == y2:
        # 왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 회전하는 경우
        for i in [-1, 1]:
            # 오른쪽, 혹은 왼쪽이 둘 다 비어 있다면
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                next_pos.append({(x1, y1), (x1, y1+i)})
                next_pos.append({(x2, y2), (x2, y2+i)})
    # 가로 => 세로 회전
    elif x1 == x2:
        # 위에서 아래로, 아래에서 위로 회전하는 경우
        for i in [-1, 1]:
            # 위쪽 혹은 아래쪽 모두 비어있다면
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                next_pos.append({(x1, y1), (x1+i, y1)})
                next_pos.append({(x2, y2), (x2+i, y2)})
    # 다음에 갈 수 있는 위치들 모두 반환
    return next_pos


def solution(board):
    n = len(board)
    # 예외처리의 편의를 위하여 주어진 위치 최외곽을 1로 채운 new_board 생성
    new_board = [[1]*(n+2) for _ in range(n+2)]
    # 중심부를 board로 대체
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_board[i][j] = board[i-1][j-1]

    # BFS Algorithm
    q = deque()
    pos = {(1, 1), (1, 2)}
    visited = []
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        # 종점을 맞닥드리면 cost를 반환하고 종료
        if (n, n) in pos:
            return cost
        # get_next_pos함수를 활용하여 bfs를 수행
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cost+1))
