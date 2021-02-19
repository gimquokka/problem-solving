
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalnum() or c in '-_.':
            # if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        # -1 인덱싱은 len(answer) == 0이면 [0:0]을 가리킴으로 굳이 조건 더 걸어줄 필요없음 Good!!
        answer = answer[:-1]
    # 5
    # if answer == '':
    if not answer:  # => 이게 좀 더 pythonic한 듯
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
