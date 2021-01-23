x = int(input())

d = [0]*30001
d[1] = 0
d[2] = 1

def divThree(x):
    if x == 1 or x == 2:
        return d[x]
    elif d[x] != 0:
        return d[x]
    f5 = x // 5
    c5 = x - f5*5 + 1
    
    f3 = x // 3
    c3 = x - f3*3 + 1

    f2 = x // 2
    c2 = x - f2*2 + 1

    if x >= 5:
        return min(c5 + divThree(f5), c3 + divThree(f3), c2 + divThree(f2))
    elif 3 <= x and x < 5:
        return min(c3 + d[f3], c2 + d[f2])

print(divThree(x))

    