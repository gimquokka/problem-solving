import sys
input = sys.stdin.readline

n = int(input())

# 각 숫자들의 개수를 담는 배열
countNumbers = [0] * 10001

for _ in range(n):
    countNumbers[int(input())] += 1

for i in range(1, 10001):

    if countNumbers[i] != 0:
        # 개수만큼 index 출력
        for _ in range(countNumbers[i]):
            print(i)