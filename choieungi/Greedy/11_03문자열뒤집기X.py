#반드시 적은 것을 뒤집는 것이 이득

n = input()
num = [0] * len(n)
location =[]

count =0

for i in range(len(n)):
    num[i] = int(n[i])

for i in range(len(n)):
    if num.count(1)>num.count(0):
        if num[i]==0:
            location.append(i)
    else:
        if num[i]==1:
            location.append(i)


temp=0

#------ 밑 부분 구현때문에 코드 짜기 실패, [1,2,3,4,5,6,7,9,10] 여기서 연속된 숫자는 연속이 끝나는 수까지 1개로 간주하고 연속되지 않은 수의 개수를 세는법
for i in range(len(location)-1):
    if location[i+1]-location[i]==1:
        temp+=1
        continue
    else:
        count+=1
    if temp>0:
        count+=1

print(count)
