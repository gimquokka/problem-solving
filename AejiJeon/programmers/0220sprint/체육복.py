def solution(n, lost, reserve):
    

    answer = n - len(lost)
    i = 0

    while i < len(lost):

        # 도난 당했지만 여벌의 체육복 존재
        if lost[i] in reserve:
            # 제외시켜줌
            reserve.remove(lost[i])
            lost.remove(lost[i])

            # 체육복 입는 학생 수 1만큼 증가
            answer += 1
        else:
            i += 1
            
    lost.sort()
    reserve.sort()
    
    i, j = 0, 0
    while i < len(lost) and j < len(reserve):

        # 빌려줄 수 있는 경우
        if lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]:
            answer += 1
            i += 1
            j += 1
        
        # 다음 학생에게 빌려줄 수 있는지 체크
        elif lost[i] - 1 > reserve[j]:
            j += 1
        
        # 다음 학생의 체육복을 빌릴 수 있는지 체크
        elif lost[i] + 1 < reserve[j]:
            i += 1
            
    return answer
