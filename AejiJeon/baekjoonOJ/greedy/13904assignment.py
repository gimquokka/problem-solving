import sys

input = sys.stdin.readline

n = int(input())
dayScores = []

for _ in range(n):
    day, score = map(int, input().split())
    dayScores.append((day, score))

# 마감일을 기준으로 오름차순 정렬,
# 마감일이 같은 경우에는 점수에 대해 내림차순으로 정렬
dayScores.sort(key=lambda x: (x[0], -x[1]))

# 포함한 과제들 중에서 제일 점수가 작은


# 여기 찾이보기!
# 포함한 과제들 중에서 제일 점수가 작은 값, index return
def get_min_score():
    temp_min = (-1, 101)
    for i in range(len(dp)):
        if dp[i] < temp_min[1]:
            temp_min = (i, dp[i])
    return temp_min


min_score = (-1, 101)
# 해당 과제가 들어갈 수 있는 index 최솟값
emptyIndex = 1
# 점수의 최댓값
sumOfScores = 0

dp = []

for dayscore in dayScores:
    day, score = dayscore
    # 해당 과제를 수행할 수 있는 날이 존재
    if emptyIndex <= day:
        dp.append(score)
        sumOfScores += score
        # 다음 과제를 넣을 index 계산
        emptyIndex += 1
    # 해당 과제를 수행할 수 있는 날이 없음
    # 다른 과제들로 꽉 찬 경우
    else:
        min_score = get_min_score()
        # 이미 채워진 과제들 중에서 제일 점수가 작은 값과 비교
        # -> 더 크다면 과제를 바꿔줌
        if min_score[1] < score:
            # 수행할 과제에서 제외된 과제의 점수를
            # total 점수에서 빼줌
            sumOfScores -= min_score[1]
            dp[min_score[0]] = score
            # 새로 추가된 과제의 점수를 더해줌
            sumOfScores += score

print(sum(dp))
