
# root of quadratic equation
import math

a, b, c = map(int, input().split())

d = b**2-4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b-math.sqrt(d)) / (2*a)
    print("%.2f" %x1)
    print("%.2f" %x2)

elif d == 0:
    x = -b / (2*a)
    print("%.2f" %x)

else:
    p1 = -b / (2*a)
    p2 = abs(math.sqrt(-d) / (2*a))
    print("%.2f+%.2fi" %(p1, p2))
    print("%.2f-%.2fi" %(p1, p2))