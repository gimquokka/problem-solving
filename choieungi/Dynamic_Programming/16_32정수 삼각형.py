n = int(input()) #n<=500

triangle = []
for i in range(n):
    temp = list(map(int,input().split()))
    triangle.append(temp)

#dp 테이블
d = [[0]*i for i in range(1,n+1)]

d[0][0] =triangle[0][0]
d[1][0] = triangle[0][0]+ triangle[1][0]
d[1][1] = triangle[0][0]+ triangle[1][1]

for i in range(2,n):
    for j in range(i+1):
        if j==0:
            d[i][j]= d[i-1][j] + triangle[i][j]
        elif j==i:
            d[i][j]= d[i-1][j-1] + triangle[i][j]
        else:
            d[i][j] = max(d[i-1][j-1]+triangle[i][j], d[i-1][j]+triangle[i][j])

result = max(d[n-1])
print(result)