# solved!

n = int(input())

drinks = []

for _ in range(n):
    drinks.append(int(input()))

d = [0]*n

# calculate d[0] 
if n >= 1:
    d[0] = drinks[0]

# calculate d[1]
if n >= 2:
    d[1] = drinks[0] + drinks[1]

# calculate d[2]
if n >= 3:
    d[2] = max(d[1], drinks[0]+drinks[2], drinks[1]+drinks[2])

# calculate from d[3] to d[n-1]
if n >= 4:
    for i in range(3, n):
        # d[i] = max amount possible to drink from drink 1 to drink k
        # first value: drink ith and (i-1)th and not drink i-2th
        # second: drink ith and not drink (i-1)th
        # third: don't drink ith
        d[i]= max(drinks[i] + drinks[i-1] + d[i-3], drinks[i] + d[i-2], d[i-1])

print(d[n-1])