def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    for move in moves:
        move -= 1
        
        for i in range(n):
            if board[i][move] != 0:
                basket.append(board[i][move])
                board[i][move] = 0
                
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.pop(-1)
                    basket.pop(-1)
                    answer += 2
                break
        
    return answer
