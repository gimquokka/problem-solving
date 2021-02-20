"""
moves 순으로 돌리면서 
board에 해당 열의 가장 상단의 값을 찾아서, 0 그 자리에 넣어주기
bucket에 넣고, 순회하면서 cnt += 1
"""


def solution(board, moves):
    size = len(board)
    bucket = []
    len_bucket = 0
    for c in moves:
        c -= 1
        for i in range(size):
            if not board[i][c]:
                continue
            else:
                bucket.append(board[i][c])
                board[i][c] = 0
                len_bucket += 1
                break

    i = 0
    answer = 0
    # while
    # (len_bucket//2+1)
    for _ in range(int(len_bucket//2+1)):
        for j in range(i, len_bucket-1):
            if bucket[j] == bucket[j+1]:
                del bucket[j:j+2]
                i = j-2
                answer += 2
                len_bucket -= 2
                break

    return answer

# 1, 2, 2, 1 => 1, 1 => x
