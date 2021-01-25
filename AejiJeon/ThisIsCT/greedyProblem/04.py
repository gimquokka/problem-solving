
# 1 1 2 3 9
# ->8
# 1  1~1    1 1~2   2 2~4  3 3~ 7    9 9 ~ 16


# 3 5 7
# -> 1
# 3 3

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

last = 0
for i in range(n):
    
    if last >= lst[i] or lst[i]-last == 1:
        last += lst[i]
    
    else:

        break

print(last+1)
