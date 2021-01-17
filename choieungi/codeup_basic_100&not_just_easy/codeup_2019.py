a, b, c = map(int, input().split())
# 파이썬에서 map()을 이용하면 몇개의 수든 받을 수 있다.

#판별식
discriminant = b**2-4*a*c

# 중근
if (discriminant== 0) :
    print("%.2f" %((-b)/(2*a)))
# 두 개 실근
elif (discriminant>0):
    print("%.2f" %(((-b)+(discriminant**0.5))/(2*a)))
    print("%.2f" %(((-b)-(discriminant**0.5))/(2*a)))
# 허근
elif (discriminant<0):
    print("%.2f+%.2fi" %((-b)/(2*a),abs(((-discriminant)**0.5)/(2*a))))
    print("%.2f-%.2fi" %((-b)/(2*a),abs(((-discriminant)**0.5)/(2*a))))

#계산 괄호 잘하기

