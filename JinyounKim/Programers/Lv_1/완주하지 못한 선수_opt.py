from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    answer = answer.keys()
    print(list(answer))
    return answer