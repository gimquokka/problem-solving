def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    n = len(participant)
    for i in range(n):
        # participant에서 completion에 없는 한 명 찾는 과정
        # sort후에 비교해주면 쉽게 찾을 수 있음
        if i == n-1 or participant[i] != completion[i]:
            return participant[i]