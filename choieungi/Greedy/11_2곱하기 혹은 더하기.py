n = input()
num = [0] * int(len(n))

result = 0

num[0] = int(n[0])
num[1] = int(n[1])
result = max(num[0]*num[1], num[0]+num[1])

for i in range(2,len(n)):
    num[i] = int(n[i])
    if result == 0 :
        result += num[i]
    else:
        if num[i] ==0 or num[i]==1:
            result += num[i]
        else:
            result *= num[i]

print(result)


#15분