from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형을 2*length 선형으로 변환
    # for i in weak: 이게 왜 안돌아가지?
    #     print(i)
    #     weak.append(i+n)
    for i in range(length):
        weak.append(weak[i]+n)
    dist_length = len(dist)
    answer = dist_length+1
    for start in range(length):
        # print('first iter')
        for friends in list(permutations(dist, dist_length)):
            # print('second iter')
            count = 1
            position = weak[start] + friends[count-1]
            for i in range(start, start+length):
                if position < weak[i]:
                    count += 1
                    if count > dist_length:
                        break
                    position = weak[i]+friends[count-1]
            answer = min(answer, count)
    if answer > dist_length:
        return -1
    return answer


# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
n = 200
weak= [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
answer = 3
print(solution(n, weak, dist))