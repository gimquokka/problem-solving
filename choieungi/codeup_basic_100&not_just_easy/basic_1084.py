a,b,c=map(int,input().split())
d=0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            d+=1
print(d)