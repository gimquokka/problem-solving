#boj_12865
#dp table == 배낭에 넣을 수 있는 물건들의 가치의 최댓값
n,k = map(int,input().split())
bag=[0]*n
d = [0]*(k+1)


for i in range(n):
    a,b  = (map(int,input().split()))
    bag[i] = (a,b)


bag.sort(key=lambda x:(x[0],-x[1]))

#print(bag)

for weight,value in bag:
        for i in range(1,d.index(max(d))+1):
        if d[i] != 0:
            try:
                d[i+weight] = max(d[i+weight],d[i]+value)
            except:
                pass
    d[weight] = max(d[weight],value)

print(d)
print(max(d))

