import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# append tuples consisting of 
# amount of drink and probability for drink to be defective
array = []

for _ in range(n):
    d, p  = map(int, input().split())
    # change percent to proportion
    array.append((d, p/100))

# sorting in decreasing order of amount of drink
array.sort(key = lambda x: (-x[0],x[1]))

# probability not to get kidnapped
# case when all drinks are not defective

probability = 1
for i in range(k):
    probability *= 1 - array[i][1]
    

# solve opposite case
result = 1 - probability


if float("%.3f" %result) < 0.001:
    print("GG")
else:
    result *= 100
    print("%.03f" %result)


