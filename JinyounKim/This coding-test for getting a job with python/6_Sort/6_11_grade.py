import sys

n = int(input())
arr = []

for i in range(n):
	name, grade = sys.stdin.readline().rstrip().split()
	arr.append((int(grade), name))

arr.sort()

print(*[n[1] for n in arr])