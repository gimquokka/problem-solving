
def solution(answers):
    result = []
    # 반복되는 부분만 담아주기
    nums1 = [1,2,3,4,5]
    nums2 = [2,1,2,3,2,4,2,5]
    nums3 = [3,3,1,1,2,2,4,4,5,5]

    # 맞은 문제 개수 담기
    c1, c2, c3 = 0, 0, 0

    for i in range(len(answers)):
        # 정답인 경우
        if nums1[i%5] == answers[i]:
            c1 += 1
        if nums2[i%8] == answers[i]:
            c2 += 1
        if nums3[i%10] == answers[i]:
            c3 += 1
    max_value = max(c1, c2, c3)

    
    if c1 == max_value:
        result.append(1)
    if c2 == max_value:
        result.append(2)
    if c3 == max_value:
        result.append(3)

    return result
