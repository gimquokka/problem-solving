#테스트 케이스
t= int(input())

#금광 정보 입력
for _ in range(t):
    n,m = map(int,input().split())
    a=0
    gold = [[0]*m for _ in range(n)]
    temp = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            gold[i][j] = temp[a+j]
        a += m

#DP table
d = [[0]*m for _ in range(n)]
for i in range(n):
    d[i][0] = gold[i][0]

#DP 진행
for j in range(1,m):
    for i in range(n):
        if i == 0:
            d[i][j] = max(d[i][j-1]+gold[i][j], d[i+1][j-1]+gold[i][j])
        elif i== n-1:
            d[i][j] = max(d[i][j-1]+gold[i][j], d[i-1][j-1]+gold[i][j])
        else:
            d[i][j] = max(d[i][j-1]+gold[i][j], d[i-1][j-1]+gold[i][j], d[i+1][j-1]+gold[i][j])

#이차원 리스트 중 최댓값 출력
result = 0
for i in range(n):
    result = max(result,d[i][m-1] )

print(result)



