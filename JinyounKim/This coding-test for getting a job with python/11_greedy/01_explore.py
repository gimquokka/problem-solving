import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

a.sort()

cont = 0
result = 0
for i in a:
	cont += 1
	if i <= cont:
		result += 1
		cont = 0
print(result)

