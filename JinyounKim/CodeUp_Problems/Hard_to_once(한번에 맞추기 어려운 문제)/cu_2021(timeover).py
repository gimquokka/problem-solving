import sys

def largest_index(arr):
	first, second = 0, 0

	for i in range(len(arr)):
		if arr[i] > first:
			first = arr[i]
		elif second < arr[i] < first:
			second = arr[i]

	first_elemet = set()
	second_elemet = set()

	for i in range(len(arr)):
		if arr[i] == first:
			first_elemet.add(i)
		elif arr[i] == second:
			second_elemet.add(i)

	return first_elemet, second_elemet

n =int(input())

arr = [0 for _ in range(1000)]

for _ in range(n):
	i = int(sys.stdin.readline())
	arr[i-1] += 1

first_elemet, second_elemet = largest_index(arr)

# Check the output
# print('arr', arr)
# print("first_elemet", first_elemet)
# print("second_elemet", second_elemet)

m = 0

if len(first_elemet) > 1:
	for f in first_elemet:
		for f1 in first_elemet:
			tmp = abs(f-f1)
			if m < tmp:
				m = tmp
else:
	for f in first_elemet:
		for s in second_elemet:
			tmp = abs(f-s)
			if m < tmp:
				m = tmp
	
print(m)

		



