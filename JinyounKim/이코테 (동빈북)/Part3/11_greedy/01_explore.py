import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

a.sort()
# 최소한의 인원이 그룹으로 포함될 때 최대의 그룹이 나온다.
cont = 0
result = 0
for i in a:
	cont += 1
	if i <= cont:
		result += 1
		cont = 0
print(result)

