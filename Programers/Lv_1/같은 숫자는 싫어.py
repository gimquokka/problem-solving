'''
- 문제
리스트에서 반복되는 수는 1개만 넣어 반복되지 않도록 함

Ex)
data = [1, 1, 1, 2, 2, 3, 2, 4,4]
=> ans = [1, 2, 3, 2, 4]
'''

def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)

    return answer
