#반드시 적은 것을 뒤집는 것이 이득

n = input()
num = [0] * len(n)

count0 =0
count1 =0

for i in range(len(n)):
    num[i] = int(n[i])

if num[0] ==1:
    count0 +=1
else:
    count1+=1

for i in range(len(num)-1): #1-->0 '1' 1회 0-->1  '0'1회
    if num[i] != num[i+1]:
        if num[i+1] ==1:
            count0 +=1
        else:
            count1+=1

print(min(count0,count1))