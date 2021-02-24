from itertools import combinations


n, m = map(int, input().split())
data = list(input().split())

data.sort()

ans = []
vowels = ['a', 'e', 'o', 'i', 'u']
# 일단 n개의 경우를 다 뽑음
for pas in combinations(data, n):
    cnt = 0

    # 모음의 개수를 측정
    for i in pas:
        if i in vowels:
            cnt += 1

    # 자음과 모음의 개수 조건이 맞으면 ans에 추가
    if 1 <= cnt and 2 <= n - cnt:
        # 원본을 정렬하고 combinations하면 사전식 순서 알아서 맞음 오오 신기!
        print(''.join(pas))
