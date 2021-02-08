from itertools import combinations

n = int(input())

a = list(map(int, input().split()))

s = set()

for i in range(1, n+1):
	for c in combinations(a, i):
		s.add(sum(c))

max_range = sum(a)

# It is not efficient compare with answer
for i in range(1, max_range):
	if i not in s: print(i)