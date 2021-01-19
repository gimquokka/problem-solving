# Get num of input and the number of input line, and Print gap between the most frequent input and second ones.
import sys
n = int(input())

frequency = dict()

for i in range(n):
	R = int(sys.stdin.readline())
	if R not in frequency:
		frequency[R] = 1
	else:
		frequency[R] += 1

first = max(frequency.values())
second = 0

for k in frequency:
	if second < frequency[k] < first:
		second = frequency[k]

f = set()
s = set()

for k in frequency:
	if frequency[k] == first:
		f.add(k)
	elif frequency[k] == second:
		s.add(k)

# print('f', f)
# print('s', s)

if len(f) > 1:
	print(max(f)-min(f))
else:
	s0 = max(f) - min(s)
	s1 = max(s) - min(f)
	print(s0 if s0 > s1 else s1)
