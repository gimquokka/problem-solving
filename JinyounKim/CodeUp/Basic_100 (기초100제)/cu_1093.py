# Get num of input and input, and print count of input by array
n = int(input())
array = list(map(int, input().split()))

check_num = [0 for _ in range(23)]

for i in array:
	check_num[i-1] += 1

print(*check_num, sep = ' ')