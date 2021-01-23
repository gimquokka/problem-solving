n = int(input())

def fact(n): 
    result = 1
    if n >= 1:
        for i in range(1, n+1):
            result *= i
    
    return result
        
count = 0
if n % 2 == 1:    # n이 홀수, 즉 2x1이 홀수개 포함
    for x in [j*2 + 1 for j in range(n//2+1)]:      # O(n)
        y = (n - x) // 2

        count += (fact(x+y)/(fact(x)*fact(y)))*(2**y)      #O(n)

else:  # n이 홀수, 즉 2x1이 홀수개 포함
    for x in [j*2 for j in range(n//2+1)]:
        y = (n - x) // 2

        count += (fact(x+y)/(fact(x)*fact(y)))*(2**y)

print(int(count)%796796)