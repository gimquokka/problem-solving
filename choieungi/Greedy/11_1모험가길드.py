n = int(input())
fear = (list(map(int, input().split())))
fear.sort()
count = 0

for i in range(n):
    temp = fear.count(i+1)
    if temp//(i+1)>0:
        count += temp//(i+1)

print(count)