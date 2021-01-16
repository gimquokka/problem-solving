# given A, # of right triangles for A < B

a = int(input())

count = 0
sq = a**2
w = 1
while True:
    if w < a:
        if sq % w == 0:
            q = sq // w
            b = (q - w) / 2
            c = (q + w) / 2


            if a < b:
                if b == int(b) and c == int(c):
                    #print(a, b, c)
                    count += 1

    else:

        break
    w += 1
print(count)
