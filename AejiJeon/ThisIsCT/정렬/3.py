n = int(input())

lst = []

for _ in range(n):
    l = input().split()
    lst.append((l[0],int(l[1])))

lst.sort(key = lambda x:x[1])
for i in range(n):
    print(lst[i][0], end = " ")