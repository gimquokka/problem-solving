#boj_13904
n= int(input())
scores = [0] * n
for i in range(n):
    a,b = map(int,input().split())
    scores[i] = (a,b)

scores.sort(key=lambda x:-x[1])

n-=1
ret = 0

to_do = [0]*1001
for deadline,score in scores:
    for k in range(deadline,0,-1):
        if to_do[k] ==0 :
            to_do[k] = score
            ret += score
            break

print(ret)



