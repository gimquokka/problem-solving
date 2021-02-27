n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+2):
        if 0 <= j-1 <= i-1 and 0 <= j <= i-1:
            data[i][j] += max(data[i-1][j-1], data[i-1][j])
        elif 0 <= j-1 <= i-1:
            data[i][j] += data[i-1][j-1]
        elif 0 <= j <= i-1:
            data[i][j] += data[i-1][j]

print(max(data[-1]))
