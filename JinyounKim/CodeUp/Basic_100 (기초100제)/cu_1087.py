# Print sum that add squentially from 1 ~ n untill sum >= input
n = int(input())

s = 0
m = 1
while(n>s):
	s += m
	if s >= n:
		print(s)
	m += 1

	
	
