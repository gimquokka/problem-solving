"""
- 문제 설명
    리스트(len: n)가 부분 연속 수열이 특정한 값(m)을 가지는 경우의 수를 구하여라
    (단. 모든 수는 양수일 때만 해결 가능)
- 전략
    1. 시작점(start)와 끝점(end)이 첫 번째 원소의 인덱스를 가르키도록 한다.
    2. 현재 부분합이 M과 같다면 cnt += 1
    3. 현재 부분합이 M보다 작으면 end를 1 증가 시킨다.
    4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
    5. 모든 경우를 확인할 때까지 2, 4의 과정을 반복한다.
"""

n = 5 # 데이터의 개수
m = 5 # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5] # 전체 수열

cnt = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    # start를 1 늘려줘야 함으로
    interval_sum -= data[start]

print(cnt)