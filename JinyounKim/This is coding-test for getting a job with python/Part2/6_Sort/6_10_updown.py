import sys

n = int(input())

arr = [0]*n

for i in range(n):
	arr[i] = int(sys.stdin.readline().rstrip())

arr.sort(reverse = True)

print(*arr, sep = ' ')