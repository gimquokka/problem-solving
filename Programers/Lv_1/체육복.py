def solution(n, lost, reserve):
    '''
    # 제한사항 5번 고려
    # 주의사항: 이렇게 for문 돌리면서 원소 지우면 정상동작하지 않음
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


a = [1, 2, 3, 4, 5]
b = [1, 2, 7, 8, 9]
for res in a:
    print(res)
    if res in b:
        b.remove(res)
        a.remove(res)
print(a, b)
