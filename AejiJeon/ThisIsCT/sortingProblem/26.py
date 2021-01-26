n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
result = (n-1)*lst[0]
for i in range(1, n):
   
    result += lst[i]*(n-i)

print(result)
