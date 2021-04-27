#2437 저울

n= int(input())
weight = list(map(int,input().split()))

weight.sort()

target =1
for i in weight:
    if target < i:
        break
    target += i
print(weight)
print(target)

