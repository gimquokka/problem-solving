"""
def find_answer(s, e, f, array):
    tmp = array[s-1:e]
    tmp.sort()
    return tmp[f-1]

def solution(array, commands):
    answer = []
    
    for s, e, f in commands:
        answer.append(find_answer(s, e, f, array))
    
    return answer
"""


def solution(array, commands): return [sorted(array[a-1:b])[c-1] for a, b, c in commands]
