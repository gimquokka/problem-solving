def solution(id):
    answer = ''
    # 1
    id = id.lower()
    
    # 2
    for c in id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c 

    # 여기서부터는 id말고 answer가지고 다룸
    # 3 내장함수 replace 사용
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5 len 함수 말고 ''랑 비교 -> 시간단축
    if answer == '':
        answer += 'a'
    
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7       
    while len(answer) < 3:
        answer += answer[-1]
            
    return answer