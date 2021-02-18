# 문제 잘못읽고 품.. -> 코드 길어짐 하하
def trans(board):
    n = len(board)
    n_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_board[j][i] = board[i][j]
    return n_board
    
def solution(board, moves):
    board = trans(board)
    answer = 0
    basket = []
    n = len(board)
    indices = [n]*n
    
    for i in range(n): 
        for j in range(n):
            if board[i][j] != 0:
                indices[i] = j
                break
     
    for move in moves: 
        move -= 1
        
        index = indices[move]
        
        # 빈 경우 
        if index == n:
            continue
        
        # 바구니에 담을 인형
        doll = board[move][index]
        
        
        # 같은 인형들 만남
        if len(basket) != 0 and basket[-1] == doll:
            basket.pop(-1)
            print(1)
            answer += 2
        # 다른 인형 만남 or 바구니 빔
        else:
            basket.append(doll)
        
        indices[move] += 1
        
        
    return answer
