# import sys
# input = sys.stdin.readline

a = list(map(int, input()))

# a.sort()
result = 0 
for i in a:
	result = max(result+i, result*i)

print(result)