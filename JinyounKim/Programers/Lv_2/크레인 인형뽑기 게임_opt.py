def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            # 이렇게 col index를 처리해주면 따로 -1을 할 필요가 없음
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    # 이렇게 -1을 이용하면 stacklist의 길이를 잴 필요가 없음
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer


"""
와 이 코드는 진짜 사기다...
"""
