def solution(participant, completion):
    c_dict = dict()
    for name in completion:
        if name not in c_dict:
            c_dict[name] = 1
        else:
            c_dict[name] += 1

    for name in participant:
        if name not in c_dict:
            answer = name
            break
        elif c_dict[name] > 0:
            c_dict[name] -= 1
        else:
            answer = name
            break

    return answer
