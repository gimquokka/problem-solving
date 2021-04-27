n = int(input())
location= [0] * n

for i in range(n):
    a,b = map(int,input().split())
    location[i] = (a,b)

location.sort(key=lambda x:(x[0],x[1]))

for i,j in location:
    print(i,j)

