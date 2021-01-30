# 시간초과 뜸
import time
start = time.time()
n = int(input())
ugly_numbers = [1]

count = 1
number = 1
while True:
    if count == n:
        break
    number += 1
    for i in [2, 3, 5]:
        if number % i == 0 and number // i in ugly_numbers:
            ugly_numbers.append(number)
            count += 1
            break
    
print(number)
print(time.time()-start)




