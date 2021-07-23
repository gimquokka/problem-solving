n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(i+1):
        data[i][j] = max(data[i][j]+data[i+1][j], data[i][j]+data[i+1][j+1])

print(data[0][0])
