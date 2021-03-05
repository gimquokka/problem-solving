from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]
