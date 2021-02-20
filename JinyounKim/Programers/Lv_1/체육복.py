def solution(n, lost, reserve):
    # 왜 여기다가 놓으면 오답지??
    # lost.sort()
    # reserve.sort()
    '''
    # 제한사항 5번 고려
    for res in reserve:
        if res in lost:
            lost.remove(res)
            reserve.remove(res)
    '''
    # 이렇게 짜는게 더 깔끔한 듯?
    _reserve = [i for i in reserve if i not in lost]
    _lost = [j for j in lost if j not in reserve]

    _lost.sort()
    _reserve.sort()
    '''
    len_lost = len(lost)
    answer = n - len_lost
    i = 0
    for res in reserve:
        for idx in range(i, len_lost):
            if res-1 <= lost[idx] <= res+1:
                answer += 1
                i = idx+1
                break
    '''
    for r in _reserve:
        b = r - 1
        a = r + 1
        if b in lost:
            lost.remove(b)
        elif a in lost:
            lost.remove(a)

    return n - len(_lost)
