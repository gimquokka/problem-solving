# print input integers until 0 apears

a = input().split()
i = 0
while 1:
    if int(a[i]) == 0: break
    print(a[i])
    i += 1