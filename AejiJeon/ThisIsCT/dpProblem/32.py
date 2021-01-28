n = int(input())
array = [] # array 자체가 dp 테이블이 됨
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    length = len(array[i])
    for j in range(length):
        if j == 0: # 맨 왼쪽
            array[i][j] += array[i-1][j]
        elif j == length-1: # 맨 오른쪽
            array[i][j] += array[i-1][j-1]
        else:
            array[i][j] += max(array[i-1][j-1], array[i-1][j])

print(max(array[n-1]))