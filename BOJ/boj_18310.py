n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[len(data)//2-1])
